#!/usr/bin/env python3
"""Compare each pinned upstream in maintenance/upstreams.json with its latest version.

Run from the repository root:

    python3 maintenance/check_upstreams.py

First it checks, offline, that the registry agrees with the repository:

- ``used_by`` names exactly the skills whose source list cites the pin;
- every commit SHA in a skill's source list is a pin in the registry;
- every audit row has exactly one row in maintenance/coverage.md, and every
  rule that coverage.md says was kept is still in a skill.

Then it queries GitHub repositories and gists with the ``gh`` CLI and Wikipedia
pages with the MediaWiki API. A GitHub entry with ``paths`` counts as changed only
when a commit after the pin touches one of those paths. Sources of kind ``manual``
print their check note. The exit status is 1 if the registry disagrees with the
repository, if any upstream has a newer version, or if a query fails.
Pass --offline to run only the first part.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from typing import NamedTuple

MAINTENANCE = Path(__file__).resolve().parent
ROOT = MAINTENANCE.parent
REGISTRY = MAINTENANCE / "upstreams.json"
MARKER = re.compile(r"<!--\s*r:([a-z0-9][a-z0-9._-]*)\s*-->")
SHA = re.compile(r"\b[0-9a-f]{40}\b")
AUDIT_ROW = re.compile(r"^\|\s*([A-Z]{2,3}-[A-Za-z0-9.\-]+)\s*\|")
USER_AGENT = "the-elements-of-style-maintenance/1.0 (https://github.com/IceCodeNew/the-elements-of-style)"


def gh(path: str, query: str) -> str:
    done = subprocess.run(
        ["gh", "api", path, "-q", query], capture_output=True, text=True, check=True
    )
    return done.stdout.strip()


def used_by_errors(registry: list[dict], skills: dict[str, str]) -> list[str]:
    """``used_by`` must name exactly the skills whose text cites the pin."""
    errors = []
    for entry in registry:
        citing = {name for name, text in skills.items() if entry["pinned"] in text}
        used_by = set(entry["used_by"]) - {"evals"}
        if citing != used_by:
            errors.append(
                f"{entry['id']}: used_by lists {sorted(used_by)}, but {sorted(citing)} cite the pin"
            )
    return errors


def unpinned_sha_errors(registry: list[dict], skills: dict[str, str]) -> list[str]:
    """Every commit SHA that a skill cites must be a pin in the registry."""
    pins = {entry["pinned"] for entry in registry}
    return [
        f"{name}: the source list cites {sha}, which is not a pin in the registry"
        for name, text in skills.items()
        for sha in sorted(set(SHA.findall(text)) - pins)
    ]


def audit_ids(audits: dict[str, str]) -> dict[str, str]:
    """Map the row ids of every audit table to their audit file; later tables repeat ids."""
    ids: dict[str, str] = {}
    for name, text in audits.items():
        for match in map(AUDIT_ROW.match, text.split("\n")):
            if match:
                ids.setdefault(match.group(1), name)
    return ids


def coverage_errors(audits: dict[str, str], coverage: str) -> list[str]:
    """Every audit row must have exactly one coverage row, and every coverage row an audit row."""
    ids = audit_ids(audits)
    rows = [m.group(1) for m in map(AUDIT_ROW.match, coverage.split("\n")) if m]
    errors = [
        f"coverage.md has {rows.count(rid)} rows for row {rid} of audits/{name}; it needs one"
        for rid, name in sorted(ids.items())
        if rows.count(rid) != 1
    ]
    errors += [
        f"coverage.md has a row for {rid}, which is in no audit"
        for rid in sorted(set(rows) - set(ids))
    ]
    return errors


def kept_rule_errors(skills: dict[str, str], coverage: str) -> list[str]:
    """Every rule that coverage.md says was kept must still be in a skill."""
    live = {rid for text in skills.values() for rid in MARKER.findall(text)}
    return [
        f"coverage.md says {rule} was kept, but no skill has that rule"
        for rule in sorted(
            set(re.findall(r"kept as `([a-z0-9._-]+)`", coverage)) - live
        )
    ]


class Repository(NamedTuple):
    registry: list[dict]
    skills: dict[str, str]  # skill name -> SKILL.md text
    audits: dict[str, str]  # audit file name -> text
    coverage: str


def load_repository() -> Repository:
    return Repository(
        json.loads(REGISTRY.read_text(encoding="utf-8")),
        {
            path.parent.name: path.read_text(encoding="utf-8")
            for path in sorted((ROOT / "skills").glob("*/SKILL.md"))
        },
        {
            path.name: path.read_text(encoding="utf-8")
            for path in sorted((MAINTENANCE / "audits").glob("*.md"))
        },
        (MAINTENANCE / "coverage.md").read_text(encoding="utf-8"),
    )


def consistency_errors(repo: Repository) -> list[str]:
    """Return every disagreement between the registry, the skills, the audits and coverage.md."""
    return (
        used_by_errors(repo.registry, repo.skills)
        + unpinned_sha_errors(repo.registry, repo.skills)
        + coverage_errors(repo.audits, repo.coverage)
        + kept_rule_errors(repo.skills, repo.coverage)
    )


class Latest(NamedTuple):
    version: str
    where: str  # a URL that shows the change since the pin, or the manual check note
    changed: bool


def _touched_since(repo: str, pinned: str, branch: str, paths: list[str]) -> bool:
    """Whether a commit after the pin touches one of the paths."""
    for path in paths:
        last = gh(
            f"repos/{repo}/commits?sha={branch}&path={path}&per_page=1",
            ".[0].sha // empty",
        )
        if last and last != pinned:
            status = gh(f"repos/{repo}/compare/{pinned}...{last}", ".status")
            if status in ("ahead", "diverged"):
                return True
    return False


def latest(entry: dict) -> Latest:
    kind = entry["kind"]
    if kind == "github":
        repo, pinned = entry["repo"], entry["pinned"]
        head = gh(f"repos/{repo}/commits/{entry['branch']}", ".sha")
        where = f"https://github.com/{repo}/compare/{pinned}...{head}"
        if head == pinned or not entry.get("paths"):
            return Latest(head, where, head != pinned)
        return Latest(
            head, where, _touched_since(repo, pinned, entry["branch"], entry["paths"])
        )
    if kind == "gist":
        gist = entry["gist"]
        version = gh(f"gists/{gist}", ".history[0].version")
        return Latest(
            version,
            f"https://gist.github.com/{entry['owner']}/{gist}/revisions",
            version != entry["pinned"],
        )
    if kind == "wikipedia":
        params = urllib.parse.urlencode(
            {
                "action": "query",
                "prop": "revisions",
                "titles": entry["page"],
                "rvprop": "ids|timestamp",
                "format": "json",
                "formatversion": "2",
            }
        )
        request = urllib.request.Request(
            f"https://en.wikipedia.org/w/api.php?{params}",
            headers={"User-Agent": USER_AGENT},
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.load(response)
        revid = str(data["query"]["pages"][0]["revisions"][0]["revid"])
        title = urllib.parse.quote(entry["page"].replace(" ", "_"))
        return Latest(
            revid,
            f"https://en.wikipedia.org/w/index.php?title={title}&diff={revid}&oldid={entry['pinned']}",
            revid != entry["pinned"],
        )
    if kind == "manual":
        return Latest(entry["pinned"], f"{entry['url']} ({entry['check']})", False)
    raise ValueError(f"unknown kind {kind!r} for {entry['id']}")


def main() -> int:
    repo = load_repository()
    errors = consistency_errors(repo)
    for error in errors:
        print(f"INVALID  {error}")
    changed = 1 if errors else 0
    if "--offline" in sys.argv[1:]:
        return changed
    for entry in repo.registry:
        try:
            found = latest(entry)
        except (subprocess.CalledProcessError, OSError, KeyError, ValueError) as error:
            detail = getattr(error, "stderr", "") or error
            print(f"ERROR    {entry['id']}: {str(detail).strip()}")
            changed = 1
            continue
        if entry["kind"] == "manual":
            status = "MANUAL"
        elif found.changed:
            status = "CHANGED"
            changed = 1
        else:
            status = "current"
        print(
            f"{status:8} {entry['id']:30} pinned={entry['pinned'][:12]:12} latest={found.version[:12]:12} {found.where}"
        )
    return changed


if __name__ == "__main__":
    sys.exit(main())

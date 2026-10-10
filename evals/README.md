# Ablation tests for the writing skills

Every rule in `skills/*/SKILL.md` stays only if a test shows that it improves the text a model writes. This directory holds the test cases, the harness that runs them, and the results. The harness needs Python 3.11 or newer.

## How a rule is tested

Each rule in a SKILL.md ends with a marker such as `<!-- r:tech.warning-placement -->`. The harness builds variants of a skill by removing marked rules, asks a model to write each test case with a variant loaded, and grades the outputs.

The person who runs the tests chooses the models that write the outputs. Use at least two models from different vendors: a rule that helps one model can show no effect on another. Every step below runs on each test model. The harness runs each call in a temporary session that loads no user settings, plugins, skills, hooks or MCP servers, and that has no tools to read files or search the web, so only the skill under test reaches the model. Codex reads a global `AGENTS.md` in `CODEX_HOME` into every prompt, so the harness refuses to run Codex while that file exists.

A rule **shows an effect** when, on the checks that test it, the pass rate with the rule is higher than without it by at least 0.2 on average, or by at least 0.4 on one check while no check drops by 0.4 or more. The second condition matters because most rules also carry checks that guard against over-applying them, and those checks pass in both variants.

1. **Screen.** Run all cases with the full skill and with the control: no skill for the genre skills, the genre skill alone for the language skills. The screen of a language skill decides only the rules of that language skill, because the genre rules are in both variants. A case that tests genre rules and also loads a language skill, because other checks in it test that language's rules, runs in one more screen of the genre skill: the language skill is loaded in both variants, and only the cases that load both skills run. A rule that shows an effect on no test model in any of these screens cannot help, so it is dropped.
2. **Leave one out.** For each rule that passed the screen, run its cases with the reduced skill and with the reduced skill minus that rule, on the genre cases and, with the language skill in both variants, on the cases that also load a language skill. A rule stays if it shows an effect on at least one test model and the summed change over all checks in its cases, across all test models, is positive. If another check drops by 0.4 or more, read its outputs: the rule stays only if the trade-off is a net gain, and `results/README.md` records the trade-off. A result between 0.1 and 0.3 is repeated with 10 repetitions before the decision.
3. **Final check.** Run all cases with the final skill and with the control. Read the outputs behind every check that does worse than the control: either the check is wrong and gets fixed, or a rule causes the drop and gets reworded or removed.
4. **Add back.** Rules can mask each other: when two rules cover the same failure, leaving out either one shows no effect. So each dropped rule whose checks did worse in the final check, or that showed an effect on one check in the screen, is added back to the final skill on its own and tested again, with the criterion of step 2.

`decide.py` applies the criteria of steps 1, 2 and 4 to the result files of all test models.

A test case is ablated the same way: a check whose pass rate never differed by 0.4 or more in any comparison is removed, and so is a case with no check left. `run.py cases --results '<glob>'...` reports this for the results files that match the globs; give every run of the current update. It marks a check without results `UNTESTED`, so run it only after every screen and ablation of the update has written its results.

`results/` is committed with the skills. It holds the results file of every run and `results/README.md`, which records each keep or drop decision and each trade-off.

## Commands

Run from the repository root. `--model` is required: a `claude` CLI model name, or `codex:<model>:<reasoning effort>` for the Codex CLI. Give an exact model ID, not an alias such as `opus`: the cache is keyed by the name, so outputs of two models behind one alias would mix. Outputs and grades are cached in `evals/.cache/`, so rerunning a command after an error or a usage limit only makes the missing calls.

```bash
python3 evals/run.py screen --skills writing-tech --tag 2026-10-s1-tech --model <model>
python3 evals/run.py screen --skills writing-tech,writing-en --control-skills writing-en --cases <ids of the cases that load both> --tag 2026-10-s1-tech-in-en --model <model>
python3 evals/run.py screen --skills writing-tech,writing-zh --control-skills writing-tech --tag 2026-10-s1-tech-zh --model <model>
python3 evals/run.py ablate --skills writing-tech --rules tech.warning-placement --tag 2026-10-s2-tech --model <model>
python3 evals/run.py inspect --skills writing-tech --case tech-runbook-upgrade-en --check warning-before-step --model <model>
python3 evals/decide.py screen-pass evals/results '2026-10-s1-tech@*' '2026-10-s1-tech-in-*@*'
python3 evals/decide.py ablate-keep evals/results '2026-10-s2-tech@*' '2026-10-s2-tech-in-*@*'
python3 evals/run.py cases --results '2026-10-*'
```

`--reps` sets the repetitions per case (default 5) and `--judge` the `claude` model that grades judge checks (default `sonnet`). If the judge refuses to grade an output, `--fallback-judge` (default `opus`) grades it. If every judge refuses, the judge checks of that output fail; if the writer refuses to write, every check of that output fails. The results file lists each of these outputs under `judge_fallbacks`, with the fallback model, `refused` or `writer-refused`, and `decide.py` marks each decision whose cases hold a refused output with `REVIEW refused`: read those outputs before you record the decision. The judge defaults are aliases, so the advice on exact model IDs applies to `--judge` and `--fallback-judge` too.

Results go to `evals/results/`. `--tag` names the run: one step of one update, such as `2026-10-s2-tech`, or one add-back rule. The file is `<kind>-<tag>@<model>.json`, so one tag gives each test model its own file. The file exists from the start of the run. A run stops if another run writes the same file, or if a run of the same tag had other settings or other skill or case texts. The runs of one tag on different models may differ only in the model, the judges and the repetitions; a rerun on the same model may change only the repetitions. A file without results binds nothing once its run has ended: if runs stopped before their first result, rerun them under the same tag, with corrected settings if needed. `decide.py` and `run.py cases --results` take globs of the tags, such as `'2026-10-s2-tech@*'` for one step on every model. Give `decide.py` one tag per skill set, and check that the files it lists under `READ` cover every test model. It stops when the files of one skill set differ in anything but the model, the judges and the repetitions; when a file holds no result yet (wait for the run, rerun it if it stopped, or delete the file if that run will not be repeated); when the files hold different rules because a model stopped or still runs; and when the shared rules of two genre skills meet in one decision. To decide the rules of a language skill, give the globs of its runs with each genre skill.

`screen --gen-only` fills the output cache without grading and writes no results file; the same command with `--tag` in place of `--gen-only` grades the cached outputs.

`tests/` at the repository root holds behavior tests of the harness and of the upstream registry. They use fake `claude` and `codex` executables and call no model. Run them after each change to `run.py`, `decide.py` or `maintenance/`:

```bash
python3 -m unittest discover -s tests -t . -v
EVALS_CONTRACT_TEST=1 python3 -m unittest discover -s tests -t . -k Contract
```

The second command calls the real `claude` CLI once. It checks that the real grader still answers in the form that the fakes assume.

To test whether an external skill would improve these skills, put it in `skills/<name>/` of a scratch copy and run `screen --skills <ours>,<name> --control-skills <ours> --all-cases --tag <name>` on each test model. The screen prints the summed change over all checks.

## Test cases

`cases/*.json` holds the cases. Each case is a writing or editing task with all its facts, the skills to load, and checks:

- `judge`: a yes/no question for the grading model, which sees the task and the output.
- `absent` / `present`: a Python regular expression that must not / must match the output.

Each check names the one rule it tests. Many cases use the examples of the sources in `maintenance/upstreams.json`.

`global-checks.json` holds anti-pattern checks from the test sources, which are anti-pattern catalogs and skills that remove signs of AI writing. They are applied to every case. Each names the rule that prevents the pattern. They are scored like case checks but never keep a case alive, and `run.py cases` never marks one for deletion. A probe case names the global checks whose patterns it tempts, as `"probe": ["<global check id>", ...]`. It runs when the rule of one of those checks is ablated, and it stays while one of those checks detects a difference.

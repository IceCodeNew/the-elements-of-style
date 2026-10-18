---
name: writing-ja
description: "Use when writing or editing Japanese text (日本語の技術文書、記事、ブログ), together with writing-tech or writing-personal. Covers Japanese wording and quotation marks."
---

# 日本語で書く

日本語に固有の規則だけをまとめる。`writing-tech` または `writing-personal` と併せて使う。

## 出典

- [k16shikano/japanese-tech-writing](https://gist.github.com/k16shikano/fd287c3133457c4fd8f5601d34aa817d), gist revision `8f2d57610a73efc97d743c9b0b0ecb1002e09fa4`, Unlicense.
- [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) @ `f4518a8eab97b8bfebc66a89d34320a89bef6930`, MIT.
- [blader/humanizer](https://github.com/blader/humanizer) v3.1.0 @ `8c307f367c91bd974002f10f2be2965d642c13df`, MIT.

## 規則

- 否定や限定の対象になる命題、引用した発言、特徴づけのために切り出す句は「」で括る（「明文化されていればすべてを任せられる」を意味しない）。地の文では " " や “ ” を使わず、「」の中でさらに括るときと書名には『』を使う。コード、コマンド、入力値の中の引用符はそのまま残す。 <!-- r:ja.kagi-quotes -->
- です・ます体の地の文では、イ形容詞に「です」を直接つけて文を終えない（「速いです」「難しかったです」「使いやすいです」）。この形が出たら、前後の文とつないで「〜は速く、〜」と続けるか、述語を動詞や名詞に替えて（「1 秒もかかりません」「手順が増えます」）、流れごと書き直す。ナ形容詞と名詞に続く「です」（「重要です」「高速です」）は対象外である。 <!-- r:ja.i-adjective-desu -->
- 設計や運用の判断を説明する地の文では、「〜してはならない」と命じる形ではなく、作業者の判断として「〜するわけにはいかない」と書く（「本番のデータを検証環境へ複製するわけにはいかない」）。手順、警告、仕様の要求事項は、命令や義務の形（「〜しないでください」「〜しなければならない」）のまま書く。 <!-- r:ja.judgment-form -->
- 英語で慣用の比喩動詞を、字義どおりの日本語に訳さない。carry →「運ぶ」、open question →「開かれた問い」、expose →「露出する」、live in →「住む」、surface →「浮上させる」、land →「着地する」、be blind to →「〜に盲目だ」がその例である。指す処理や状態をそのまま書く（「この情報は残差ストリームに住んでいる」→「この情報は残差ストリームに含まれる」）。 <!-- r:ja.calque-verbs -->

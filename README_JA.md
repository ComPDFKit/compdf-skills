![ComPDF-Comprehensive PDF Solutions](images/ComPDF-ComprehensivePDFSolutions.png)

[English](README.md) | [繁體中文](README_TW.md) | [日本語](README_JA.md) | [简体中文](README_CN.md)

# ComPDF Skills

**ComPDF Skills** は、AI Agent 向けに **PDF/画像の解析、データ抽出、ドキュメント形式変換、PDF 処理機能** を提供し、ドキュメント自動化ワークフロー全体の構築を支援します。大規模言語モデルによる推論の前段で、ComPDF Skills が文書解析、OCR、データ抽出、構造化前処理を実行し、非構造化ファイルを AI がそのまま理解できるデータへ変換します。必要な内容だけをモデルに渡せるため、Token 消費とモデル利用コストを抑えながら、Agent のドキュメント処理効率と回答品質を大きく高められます。

> - ComPDF Skills があなたのワークフローに役立ったら、GitHub で ⭐ **Star** を付けていただけると嬉しいです。
> - ご質問、ご提案、導入に関するご相談は、**Issues** と **Discussions** からお気軽にお寄せください。

<p align="center">
  <a href="https://github.com/ComPDFKit/compdf-skills"><img src="https://img.shields.io/github/stars/ComPDFKit/compdf-skills?style=social" alt="GitHub Stars"></a>
  <a href="#"><img src="https://img.shields.io/badge/Agent%20Skills-Ready-3863F1" alt="Agent Skills Ready"></a>
  <a href="#"><img src="https://img.shields.io/badge/License-Free%20to%20Start-FF8A00" alt="Free to Start"></a>
</p>

<p align="center">
  <a href="#compdf-skills-を選ぶ理由"><b>ComPDF Skills を選ぶ理由</b></a> •
  <a href="#主な機能"><b>主な機能</b></a> •
  <a href="#license-と無料利用"><b>License と無料利用</b></a> •
  <a href="#インストールと有効化"><b>インストールと有効化</b></a> •
  <a href="#利用シーンとサンプル指示"><b>利用シーン</b></a> •
  <a href="#サポート"><b>サポート</b></a>
</p>

## ComPDF Skills を選ぶ理由

- AI ドキュメント処理に特化した機能群：PDF/画像解析、OCR、データ抽出、形式変換、ページ処理などに対応し、非構造化ドキュメントを AI Agent がそのまま扱える構造化データへ変換します。複雑な文書でも、より正確に処理できます。

- より効率的で低コストな AI ワークフロー：モデル推論の前に文書解析と前処理を完了し、必要な情報だけを LLM に渡すことで、Token 消費とモデル利用コストを抑えつつ、応答速度と処理効率を高めます。

- 豊富な出力形式に対応：Word、Excel、PowerPoint、HTML、Markdown、JSON、CSV、RTF、TXT、画像などに対応し、さまざまな Agent ワークフローや業務システム間のデータ連携に活用できます。

- 無料で始めやすく、価値を検証しやすい：毎月の無料ドキュメント処理枠が用意されており、日常業務の中で導入効果を無理なく確認できます。

## 主な機能

ComPDF Skills は、ドキュメント変換、PDF 操作、インテリジェントな解析とデータ抽出機能を Agent 向けに提供します。詳細は以下のとおりです。

### 1. PDF 解析とデータ抽出

| 機能 | 説明 |
| --- | --- |
| 画像解析とデータ抽出 | 画像ファイルからテキスト、表、項目、構造化コンテンツを抽出し、後続の AI ワークフローや自動化に活用できます。 |
| PDF 解析とデータ抽出 | PDF ファイルからテキスト、表、項目、構造化コンテンツを抽出し、後続の AI ワークフローや自動化に活用できます。 |

### 2. PDF と画像の変換

| 機能 | 説明 |
| --- | --- |
| PDF から Word | PDF ファイルを編集可能な Word 文書へ変換し、元のレイアウト、テキスト、画像、書式をできる限り保持します。 |
| PDF から Excel | PDF ファイルを Excel に変換し、表、数値、構造化された業務データに対応します。 |
| PDF から PPT | PDF ページを編集可能な PowerPoint スライドへ変換し、元のレイアウトと視覚構造をできる限り保持します。 |
| PDF から HTML | PDF ファイルを HTML へ変換し、Web 表示やコンテンツ再利用に活用できます。テキスト、画像、表、レイアウトも可能な限り保持します。 |
| PDF から RTF | PDF ファイルを RTF 文書へ変換し、テキストと画像コンテンツに対応します。 |
| PDF から画像 | PDF ページを PNG、JPG、JPEG、JPEG2000、BMP、TIFF、TGA、GIF、WEBP 画像へ変換し、解像度や DPI の設定にも対応します。 |
| PDF から CSV | PDF ファイルから表を抽出して CSV として出力します。表ごとの出力にも、まとめての出力にも対応します。 |
| PDF から TXT | PDF またはスキャン PDF からテキストを抽出し、プレーンテキストとして保存します。 |
| PDF から JSON | PDF ファイルからテキスト、表、画像を抽出し、構造化 JSON として保存します。 |
| PDF から Markdown | PDF ファイルを Markdown に変換し、ナレッジベース、開発ドキュメント、ブログ、AI ワークフローでの再利用を容易にします。 |
| PDF から検索可能 PDF | スキャン PDF に OCR を実行し、検索、コピー、ハイライト可能な PDF を出力します。検索、保管、後続処理に適しています。 |
| PDF から検索可能 OFD | スキャン PDF に OCR を実行し、検索可能な OFD ファイルへ変換します。OFD の保管、回覧、ローカル業務シーンに適しています。 |
| Word から PDF | Word 文書を PDF に変換し、レイアウト、フォント、画像、ページ構造をできる限り保持します。共有、保管、印刷に適しています。 |
| PNG から PDF | PNG 画像を PDF に変換し、スクリーンショット、デザイン素材、証跡画像の整理、共有、保管に便利です。 |
| RTF から PDF | RTF 文書を PDF に変換し、基本的な文字スタイルやレイアウトを保ちながら、デバイスを問わず安定した出力を実現します。 |
| Excel から PDF | Excel ブックやスプレッドシートを PDF に変換し、レポート共有、印刷、保管、誤編集防止に役立ちます。 |
| TXT から PDF | プレーンテキストを PDF に変換し、ログ、メモ、手順書などを固定レイアウト文書として整理できます。 |
| CSV から PDF | CSV データを PDF に変換し、スナップショット共有、確認、印刷、業務保管に利用できます。 |
| PPT から PDF | PowerPoint プレゼンテーションを PDF に変換し、配布、デバイスをまたいだ閲覧、正式な保存に適しています。 |
| HTML から PDF | HTML ページやコンテンツ断片を PDF に変換し、Web ページ保存、レポート出力、メールアーカイブ、印刷用出力に活用できます。 |
| 画像から Word | JPG、JPEG、PNG、BMP 画像を編集可能な Word 文書へ変換します。 |
| 画像から Excel | 画像ファイルを Excel ブックへ変換し、表、テキスト、数値コンテンツに対応します。 |
| 画像から PPT | 画像ファイルを編集可能な PowerPoint スライドへ変換し、見たままのレイアウトと内容構造をできる限り保持します。 |
| 画像から PDF | JPG、JPEG、PNG、BMP などの画像を PDF に変換し、複数画像の取りまとめ、共有、印刷、保管に便利です。 |
| 画像から HTML | 画像ファイルを HTML に変換し、テキスト、レイアウト、表、主要な視覚要素を可能な限り保持します。 |
| 画像から RTF | 画像ファイルを RTF 文書へ変換し、抽出したテキストや画像コンテンツに対応します。 |
| 画像から CSV | 画像ファイルから表を抽出して CSV として出力します。 |
| 画像から TXT | 画像ファイルからテキストを抽出し、プレーンテキストとして保存します。 |
| 画像から JSON | 画像ファイルからテキスト、表、画像を抽出し、構造化 JSON として保存します。 |

### 3. PDF 編集と保護

| 機能 | 説明 |
| --- | --- |
| PDF の結合 | 複数の PDF ファイルを 1 つの PDF 文書に結合します。 |
| PDF の分割 | 1 つの PDF ファイルを複数の小さな PDF に分割します。 |
| PDF ページの回転 | 選択した PDF ページを 90、180、270 度回転します。 |
| PDF ページの挿入 | 既存の PDF に空白ページ、画像ページ、または他の PDF のページを挿入します。 |
| PDF ページの削除 | PDF ファイル内の 1 ページまたは複数ページを削除します。 |
| PDF ページの抽出 | 選択したページまたはページ範囲を抽出し、新しいファイルとして保存します。 |
| 透かしの追加 | PDF ファイルにテキストまたは画像の透かしを追加し、ブランド表示や利用制御に活用できます。 |
| 透かしの削除 | 対応する PDF ファイルからテキストまたは画像の透かしを削除します。 |
| PDF の暗号化 | AES 暗号化と権限制御で PDF ファイルを保護します。 |
| PDF の復号 | 権限がある場合に限り、PDF ファイルのパスワードを解除して内部処理や再利用をしやすくします。 |

## License と無料利用

ComPDF Skills をインストール後、[License を取得](https://www.compdf.com/compdf-portal/signin?utm_source=github&utm_medium=referral&utm_campaign=compdf_skills_repo_ja&ref_platform_id=github_compdfkit_skills_ja) し、API Key を Agents に渡すことで無料で利用を開始できます。

![get-license](./images/get-license.png)

## インストールと有効化

まずは GitHub Skills リポジトリからインストールし、各 Skill ディレクトリを `SKILL.md`、`docs/`、`scripts/` などの関連ファイルごと保持することをおすすめします。公開リポジトリ URL がまだ確定していない場合は、以下のプレースホルダーを正式なリポジトリ URL またはパスに置き換えてください。

### 1. GitHub から Skills を取得

方法 1：Agent Skills 標準に対応したプラットフォームでは、リポジトリパスから直接インストールできます。

```bash
npx skills add <owner>/<repo>/skills -y
```

方法 2：GitHub リポジトリを手動で clone またはダウンロードし、対象 Skill フォルダをコピーします。

```bash
git clone https://github.com/ComPDFKit/compdf-skills.git
```

対象 Skill ディレクトリを、各 Agent が対応する Skills / Rules ディレクトリにコピーし、フォルダ構成はそのまま保持してください。

### 2. 主要 Agent 製品での有効化方法

#### Claude Code

1. Claude Code をインストールし、サインインします。
2. GitHub Skills からインストールするか、公開済みの Skill インストールコマンドを使います。
3. リポジトリフォルダ方式を使う場合は、Skill フォルダを Claude Code の skills ディレクトリへ配置し、セッションを再起動します。
4. 自然言語でタスクを入力するか、Skill 名を明示して呼び出します。

プラットフォーム側で公開済みの導線がある場合は、以下のようなコマンド形式になります。

```bash
claude skill add <namespace>/<skill-name>
claude skill install <skill-url>
```

#### Windsurf

1. プロジェクトのワークスペースを開きます。
2. GitHub から取得した Skill フォルダを `.windsurf/skills/compdf-skills/`、またはクロス Agent 互換パスである `.agents/skills/compdf-skills/` に配置します。
3. ディレクトリ内に `SKILL.md` と必要な付属ファイルが含まれていることを確認します。
4. Cascade を開くと、Windsurf が自動的に Skill を検出します。
5. タスクをそのまま入力して自動起動させるか、`@compdf-skills` で手動起動します。

#### Cline

1. Cline をインストールして開きます。
2. GitHub から取得した Skill フォルダを、プロジェクト単位の `.cline/skills/compdf-skills/`、またはグローバルの `~/.cline/skills/compdf-skills/` に配置します。
3. Cline パネルを開き、Skills エントリから Skill が検出・有効化されていることを確認します。
4. 自然言語でタスクを入力するか、`/compdf-skills` で明示的に呼び出します。

#### Cursor

Cursor の現行公式ワークフローは、独立した Skills ディレクトリよりも Rules と `AGENTS.md` を重視しています。

1. ComPDF Skills GitHub リポジトリから主要な説明ファイルを取得します。
2. 共通ガイダンスを `.cursor/rules/compdf-skills.mdc` のようなプロジェクトルールに変換するか、プロジェクトルートに `AGENTS.md` を置いて互換レイヤーとして利用します。
3. Cursor Agent / CLI を開くと、設定に応じてルールが自動的に読み込まれます。
4. 変換、抽出、OCR、透かし追加などのタスクを Agent に依頼すれば利用できます。

#### 社内 Agent プラットフォーム

1. ComPDF Skills の GitHub リポジトリを社内のソース管理またはアーティファクト基盤へミラーします。
2. `SKILL.md`、バージョン情報、License ファイル、補助スクリプトを 1 つの管理パッケージとして維持します。
3. 社内 Agent プラットフォームに Skills ディレクトリをマウントするか、主要な説明をプラットフォーム向けルールテンプレートへ変換します。
4. 「ComPDF 前処理 + AI 推論」の流れを推奨します。まず解析・変換・抽出を行い、その結果をモデルへ渡してください。

## 利用シーンとサンプル指示

PDF、画像、またはその他の元ファイルをアップロードし、表抽出、形式変換、PDF 結合、透かし追加などの指示を入力してください。Agent が対応する ComPDF Skill を呼び出して結果を返します。さらに分析が必要な場合は、処理後の出力を AI に渡してください。

利用シーン：

* ChatGPT、カスタム Agent、社内 Agent プラットフォームなど、Skills を扱える環境で、レポート、ホワイトペーパー、提案書 PDF をまず Markdown や Word に変換し、その後 AI に要約、要点整理、構成再編を依頼する
* 請求書、明細書、スキャン表、画像添付ファイルを扱う Skills ワークフローで、まず表や構造化データを抽出し、その後に経理レビュー、精算準備、システム入力、自動振り分けを進める
* 契約書、入札資料、見積書、納品ファイル、保管文書などを Agent ワークフローで整理する際に、先に PDF の結合、分割、透かし追加、形式変換を行い、その後 AI に整理、命名、外部送付準備を任せる
* 多段階ワークフローでは、PDF や画像をまず CSV、JSON、TXT、Markdown などの軽量出力へ変換し、その後の Agent に項目整理、ナレッジ登録、承認フロー処理、自動化オーケストレーションを担当させる

**サンプル指示：**

* この PDF を Word に変換し、レイアウトをできるだけ保持してください。
* この PDF 内のすべての表を抽出して CSV として出力してください。
* この画像を JSON に変換し、構造化データとして返してください。
* これらの PDF を結合し、透かしを追加して最終ファイルを返してください。
* このレポートをまず Markdown に変換し、その後で要点を要約してください。

## サポート

ご質問やご提案がありましたら、以下をご利用ください。

- `Issue` を投稿する
- `Discussions` に参加する
- [ComPDF チームにお問い合わせ](https://www.compdf.com/contact-sales?utm_source=github&utm_medium=referral&utm_campaign=compdf_skills_repo_ja&ref_platform_id=github_compdfkit_skills_ja)いただき、商用ライセンス、企業導入、大規模展開について相談する

ComPDF Skills があなたのワークフローに役立ったら、ぜひ ⭐ **Star** をお願いします。

---

<p align="center">
  <b>ComPDF チームがお届けします。</b><br>
  <a href="https://www.compdf.com/?utm_source=github&utm_medium=referral&utm_campaign=compdf_skills_repo_ja&ref_platform_id=github_compdfkit_skills_ja">公式サイト</a> ·
  <a href="https://www.compdf.com/contact-sales?utm_source=github&utm_medium=referral&utm_campaign=compdf_skills_repo_ja&ref_platform_id=github_compdfkit_skills_ja">営業に問い合わせる</a> ·
  <a href="#インストールと有効化">インストールと有効化</a>
</p>

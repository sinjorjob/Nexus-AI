# Nexus-AI
Multi-agent application using OpenAI's Swarm

# Django チャットボットアプリケーション

このプロジェクトは、OpenAI のSWARM（マルチエージェントライブラリ）を使ったDjango ベースのチャットボットアプリケーションです。

## 推奨

- Python 3.11 以上

## セットアップ手順

1. リポジトリをクローンする：
   ```
   git clone https://github.com/sinjorjob/Nexus-AI.git
   cd Nexus-AI
   ```

2. 仮想環境を作成し、アクティベートする：
   ```
   python -m venv venv
   venv\Scripts\activate`
   ```

3. 必要なパッケージをインストールする：
   ```
   pip install -r requirements.txt
   ```

4. 環境変数を設定する：
   - プロジェクトのルートディレクトリに `.env` ファイルを作成し、以下の内容を追加：
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. データベースをマイグレーションする：
   ```
   python manage.py migrate
   ```

6. 初期データをロードする：
   ```
   python manage.py load_init_data
   ```

## アプリケーションの起動

1. 開発サーバーを起動する：
   ```
   python manage.py runserver
   ```

2. ブラウザで `http://127.0.0.1:8000` にアクセスする。

## 使用方法

- メインページ (`/`) でチャットボットとの対話を開始できます。
- エージェントが保持する知識（instructionsの情報）を更新するには、`/update-instructions-view/` にアクセスするかadmin画面で直接修正してください。

## プロジェクト構造

```
config/             # プロジェクト設定
chatbot/            # メインアプリケーション
├── fixtures/       # 初期データ
├── management/     # カスタム管理コマンド
├── migrations/     # データベースマイグレーション
├── templates/      # HTML テンプレート
├── admin.py        # 管理サイト設定
├── agents.py       # エージェント関連の機能
├── models.py       # データベースモデル
├── urls.py         # URL 設定
├── utils.py        # ユーティリティ関数
└── views.py        # ビュー関数
manage.py           # Django 管理スクリプト
requirements.txt    # 依存パッケージリスト
```

## 注意事項

- このアプリケーションはあくまでSWARMの検証目的のコードです。
　本番利用はしないでください。


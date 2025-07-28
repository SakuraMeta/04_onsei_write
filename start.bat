@echo off
echo 🎤 リアルタイム音声文字起こしアプリを起動しています...
echo.

REM 仮想環境の確認・作成
if not exist "venv" (
    echo 仮想環境を作成しています...
    python -m venv venv
)

REM 仮想環境をアクティベート
call venv\Scripts\activate

REM 依存関係のインストール
echo 依存関係をインストールしています...
pip install -r requirements.txt

REM アプリケーションを起動
echo.
echo アプリケーションを起動しています...
echo ブラウザで http://localhost:5000 にアクセスしてください
echo.
python app.py

pause

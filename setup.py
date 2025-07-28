import subprocess
import sys
import os

def install_requirements():
    """必要なパッケージをインストール"""
    print("必要なパッケージをインストールしています...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ パッケージのインストールが完了しました")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ パッケージのインストールに失敗しました: {e}")
        return False

def check_microphone():
    """マイクの動作確認"""
    print("\nマイクの動作確認を行います...")
    try:
        import speech_recognition as sr
        r = sr.Recognizer()
        
        # マイクデバイスの一覧表示
        mic_list = sr.Microphone.list_microphone_names()
        print(f"利用可能なマイクデバイス数: {len(mic_list)}")
        
        if len(mic_list) > 0:
            print("✅ マイクデバイスが検出されました")
            return True
        else:
            print("❌ マイクデバイスが見つかりません")
            return False
            
    except Exception as e:
        print(f"❌ マイクの確認中にエラーが発生しました: {e}")
        return False

def main():
    print("🎤 リアルタイム音声文字起こしアプリのセットアップ")
    print("=" * 50)
    
    # 1. パッケージインストール
    if not install_requirements():
        return
    
    # 2. マイク確認
    if not check_microphone():
        print("\n⚠️  マイクの設定を確認してください")
        print("   - マイクが接続されているか確認")
        print("   - プライバシー設定でマイクアクセスが許可されているか確認")
    
    print("\n🚀 セットアップ完了！")
    print("アプリを起動するには以下のコマンドを実行してください:")
    print("python app.py")
    print("\nブラウザで http://localhost:5000 にアクセスしてください")

if __name__ == "__main__":
    main()

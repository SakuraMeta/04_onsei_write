from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import time
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

# 文字起こし履歴を保存
transcription_history = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('クライアントが接続しました')
    emit('status', {'message': '接続完了'})
    # 過去の文字起こし履歴を送信
    for item in transcription_history:
        emit('transcription', item)

@socketio.on('disconnect')
def handle_disconnect():
    print('クライアントが切断しました')

@socketio.on('transcription_result')
def handle_transcription_result(data):
    """ブラウザからの文字起こし結果を受信"""
    try:
        transcription_item = {
            'text': data['text'],
            'timestamp': time.time(),
            'confidence': data.get('confidence', 0)
        }
        
        # 履歴に保存
        transcription_history.append(transcription_item)
        
        # 他のクライアントにブロードキャスト
        emit('transcription', transcription_item, broadcast=True)
        
        print(f"文字起こし結果: {data['text']}")
        
    except Exception as e:
        emit('error', {'message': f'処理エラー: {str(e)}'})

@socketio.on('clear_history')
def handle_clear_history():
    """履歴をクリア"""
    global transcription_history
    transcription_history = []
    emit('history_cleared', broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)

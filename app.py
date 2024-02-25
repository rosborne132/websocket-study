from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message_from_client')
def handle_message(message):
    print('Received message from client:', message)
    # Echo the message back to the client
    emit('message_from_server', message)

if __name__ == '__main__':
    socketio.run(app)
    
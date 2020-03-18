from flask import Flask
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO, send
import os


template_dir = '../templates'
static_dir = '../static'
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config['SECRET_KEY'] = os.urandom(24)
socketio = SocketIO(app)
bootstrap = Bootstrap(app)


@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


from app import views

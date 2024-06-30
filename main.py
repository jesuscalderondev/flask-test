from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socket = SocketIO(app)

@app.route('/')
def index():
    return render_template('test.html')


if __name__ == '__main__':
    socket.run(app)

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import qrcode
import socket

app = Flask(__name__)
socketio = SocketIO(app)

# Find an open port dynamically
def find_open_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))  # Bind to any available port
        return s.getsockname()[1]  # Get the assigned port number

# Generate QR Code for the form
def generate_qr_code(ip, port):
    url = f"http://{ip}:{port}"
    qr = qrcode.make(url)
    qr.save("form_qr_code.png")
    print(f"QR code generated for: {url}")

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text']
    print(f"Received text: {text}")  # Log the submission in the terminal
    socketio.emit('new_message', {'text': text}, to='/')
    return "Message received!", 200



@socketio.on('connect')
def on_connect():
    print('A user connected.')

if __name__ == '__main__':
    # Find the local IP address
    host_ip = socket.gethostbyname(socket.gethostname())
    # Find an open port
    open_port = find_open_port()
    # Generate the QR code with the host IP and open port
    generate_qr_code(host_ip, open_port)
    # Run the server on the found open port
    socketio.run(app, host='0.0.0.0', port=open_port)

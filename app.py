from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET'])
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
    return send_from_directory('html', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)


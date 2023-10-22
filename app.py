from flask import Flask, jsonify, request, send_from_directory, render_template
from flask_socketio import SocketIO
import os

app = Flask(__name__, static_folder='static/static')
socketio = SocketIO(app)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True
app.debug = True


# Route to switch everything into my proxy
@app.route('/api/')
def index():
    # return render_template('index.html')
    return send_from_directory('static', 'index.html')



# Routes to handle navigation
@app.route('/api/process', methods=['POST'])
def process():
    data = request.get_json()
    text = data.get('text')
    altered_text = text.upper()

    return jsonify({'processed_text': altered_text})

@app.route('/api/load-page')
def load_page():
    page = request.args.get('page')
    return render_template(page + '.html')



# Route testing
@app.route('/api/testing')
def test():
    response_body = {
        "response": "This is online!"
    }
    return response_body

@app.route('/testing')
def test_local():
    response_body = {
        "response": "This is online!"
    }
    return response_body

if __name__ == '__main__':
    # Use the environment variable PORT if it exists, otherwise use a default port (e.g., 5000)
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app)

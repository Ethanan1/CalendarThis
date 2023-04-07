import flask import flask

app = Flask(__calendar_this__)


@app.route('/')
def index():
    return '<h1>Sample App</h1>'

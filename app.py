from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    name = 'Brian'
    # name.append('Stanton')
    return f'Hello {name}!!!!'

@app.route('/test')
def test():
    return 'This is a test!'

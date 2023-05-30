from app import app
from flask import render_template


@app.route('/')
def index():
    name = 'Brian'
    # name.append('Stanton')
    return render_template('index.html', first_name=name)

@app.route('/test')
def test():
    return 'This is a test!'

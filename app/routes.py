from app import app
from flask import render_template


@app.route('/')
def index():
    name = 'Brian'
    # name.append('Stanton')
    countries = ['United States', 'Mexico', 'Canada', 'China', 'Japan', 'France']
    return render_template('index.html', first_name=name, countries=countries)

@app.route('/test')
def test():
    return 'This is a test!'

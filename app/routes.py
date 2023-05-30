from app import app


@app.route('/')
def index():
    name = 'Brian'
    # name.append('Stanton')
    return f'Hello {name}!!!!'

@app.route('/test')
def test():
    return 'This is a test!'

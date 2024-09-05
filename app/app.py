from flask import Flask, render_template
from db import get_users
from file_section import hello_world

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/file_section')
def file_section():
    return hello_world()

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/users')
def users():
    return get_users()

if __name__ == '__main__':
    app.run()

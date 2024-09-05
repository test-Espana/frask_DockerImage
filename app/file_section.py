# app/hello.py


from flask import render_template

def hello_world():
    return render_template('hello.html')

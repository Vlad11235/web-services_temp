from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    print('Hello')  # пишется в командную строку
    return "Hello, mr dgdfg gdfg dfgdfgs dfgdfgdf world!"

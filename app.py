from flask import Flask
from markupsafe import escape
import os
app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the landing page.'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/apps/launch/<exe_name>')
def app_launch(exe_name):
    # Launch an application that's in PATH
    os.system('start ' + escape(exe_name))
    return f"Launching {exe_name}"
from flask import Flask, request, jsonify
from markupsafe import escape
import os

app = Flask(__name__)
app.config["DEBUG"] = True

scripts = [
    {'id': 0,
    'name': 'unlock-adaccount.ps1',
    'language': 'powershell',
    'description': 'Unlock a user\'s Active Directory account'},
    {'id': 1,
    'name': 'restart-vm.ps1',
    'language': 'powershell',
    'description': 'Restart a single virtual machine'}
]


@app.route('/', methods=['GET'])
def index():
    return '<h1>This is the landing page.</h1>'

@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/apps/launch/<exe_name>', methods=['POST'])
def app_launch(exe_name):
    """Launch an application that's in PATH"""
    os.system('start ' + escape(exe_name))
    return f"Launching {exe_name}"

# -------------- API
@app.route('/api/v1/resources/scripts/all', methods=['GET'])
def scripts_all():
    return jsonify(scripts)

@app.route('/api/v1/resources/scripts', methods=['GET'])
def scripts_id():
    """
    Check if an ID was provided as part of the URL.
    If ID is provided, assign it to a variable.
    If no ID is provided, display an error in the browser.
    """
    if 'id' in request.args:
        id = int(request.args['id'])
    elif 'fart' in request.args:
        return "Fart received."
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for script in scripts:
        if script['id'] == id:
            results.append(script)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@app.route('/api/v1/authenticate', methods=['POST'])
def authenticate():
    """
    Authenticate user to see if they're allowed to make further requests.
    """
    return jsonify(None)

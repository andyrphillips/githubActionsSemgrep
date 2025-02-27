import os
import subprocess
import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/exec')
def execute_command():
    # VERY obvious command injection
    cmd = request.args.get('cmd')
    os.system(cmd)  # This should definitely be caught
    return "Command executed"

@app.route('/read')
def read_file():
    # VERY obvious path traversal
    filename = request.args.get('file')
    with open(filename, 'r') as f:  # This should definitely be caught
        return f.read()

if __name__ == '__main__':
    app.run(debug=True)
import os
import subprocess
import flask
from flask import request
from pathlib import Path

app = flask.Flask(__name__)

@app.route('/exec')
def execute_command():
    # Very obvious command injection
    cmd = request.args.get('cmd')
    os.system(cmd)
    return "Command executed"

@app.route('/read')
def read_file():
    # Very obvious path traversal
    filename = request.args.get('file')
    
    with open(filename, 'r') as f:
        return f.read()

    

if __name__ == '__main__':
    app.run(debug=True)
import os
import subprocess
import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/search')
def search():
    # SECURITY ISSUE: Command injection vulnerability
    query = request.args.get('q', '')
    result = subprocess.call("grep -r " + query + " /app/data", shell=True)
    return str(result)

@app.route('/user/<username>')
def user_profile(username):
    # SECURITY ISSUE: Potential path traversal
    with open(f"/app/data/{username}", "r") as f:
        return f.read()

if __name__ == '__main__':
    app.run(debug=True)
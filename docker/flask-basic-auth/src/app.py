#!/usr/bin/env python3

from flask import Flask
from flask_basicauth import BasicAuth

app = Flask(__name__)

# Default values for the username and password
app.config['BASIC_AUTH_USERNAME'] = 'john'
app.config['BASIC_AUTH_PASSWORD'] = 'matrix'

# Force basic auth in all the website
app.config['BASIC_AUTH_FORCE'] = True

# Initialize the basic auth
basic_auth = BasicAuth(app)


@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'


if __name__ == "__main__":
    app.run(debug=True)

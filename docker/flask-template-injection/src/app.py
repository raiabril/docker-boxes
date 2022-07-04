#!/usr/bin/env python3

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_geek():
    
    user = request.args.get('user')

    return render_template("index.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)
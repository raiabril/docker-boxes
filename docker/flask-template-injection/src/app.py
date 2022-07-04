#!/usr/bin/env python3

from flask import Flask, request, render_template, render_template_string
app = Flask(__name__)

@app.route('/')
def hello_geek():
    
    user = request.args.get('user')

    if user:
        template = "Hello %s" % user

    else:
        template = f"Say the magic word!"

    return render_template_string(template, user=user)

if __name__ == "__main__":
    app.run(debug=True)
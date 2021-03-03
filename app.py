from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    """Return "welcome" greeting."""

    html = "<html><body><h1>Welcome</h1></body></html>"
    return html


@app.route('/welcome/home')
def welcome_home():
    """Welcomes you home."""

    html = "<html><body><h1>Welcome home</h1></body></html>"
    return html


@app.route('/welcome/back')
def welcome_back():
    """Welcomes you back."""

    html = "<html><body><h1>Welcome back</h1></body></html>"
    return html


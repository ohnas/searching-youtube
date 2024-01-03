from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/oauth2Callback")
def callback():
    return "success callback"

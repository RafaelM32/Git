from flask import Flask, make_response

app = Flask(__name__)

@app.route("/")
def hello():
    return make_response("hello word")
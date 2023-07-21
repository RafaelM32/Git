from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello word"


app.run(port=3000)
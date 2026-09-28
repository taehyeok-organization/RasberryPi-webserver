from flask import Flask
import config

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/hello")
def hello():
    return "hello world"


@app.route("/hi")
def hi():
    return "hi world"

@app.route("/sum/<int:a>/<int:b>")
def sum(a, b):
    return str(a + b)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=True) 

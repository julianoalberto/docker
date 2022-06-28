from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/add")
def add():
    a = request.args.get("a", default=0, type=int)
    b = request.args.get("b", default=0, type=int)
    return f"{a} + {b} = {a + b}\n"

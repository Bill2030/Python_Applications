
from flask import Flask

app = Flask(__name__)


@app.route('/')
def Hello__World():
    return "<p>Hello World</p>"





from os import environ
from flask import Flask, abort, request
from flask_cors import CORS

import sentiment


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, DivHacksMLBackend!</p>"

@app.route("/yay", methods=["POST"])
def create():
    request_data = request.get_json()
    if "name" in data:
        abort(400)
    else:
        data = sentiment.yay(request_data["name"])
        return {"yay": data}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=environ["PORT"])

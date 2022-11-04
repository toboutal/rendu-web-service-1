from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/")
def hello_first_api():
    data = {
        "message": "hello first api",
    }
    return data;


@app.route("/list", methods=["POST"])
def liste():
    return request.json

import flask
import signature
from flask import request

app = flask.Flask("Signature API")


@app.route("/signature", methods=["POST"])
def home():
    signature.helloWorld()   
    print(request.json) 
    return "Coolio"

app.run()
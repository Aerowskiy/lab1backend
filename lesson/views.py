from flask import Flask, jsonify
from datetime import datetime
from lesson import app

@app.route("/")
def all_works():
    return f"<p>all works!</p><a href='/healthcheck'>Health Status</a>"


@app.route("/healthcheck")
def healthcheck():
    resp = jsonify(date=datetime.now(), status="OK")
    resp.status_code = 200
    return resp

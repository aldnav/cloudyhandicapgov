
""" MAIN APP SERVER """

import json
from flask import Flask, render_template, Response
app = Flask(__name__)


@app.route("/")
def index():
    """ Displays index page """
    return render_template('index.html')


@app.route("/api/reports/")
def fetch():
    """ Reports are returned here """
    data = {}
    return Response(
        response=json.dumps(data), status=200, mimetype="application/json")


if __name__ == "__main__":
    app.debug = True
    app.run()

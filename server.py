
""" MAIN APP SERVER """

import json
from flask import Flask, render_template, Response, request
app = Flask(__name__)


@app.route("/")
def index():
    """ Displays index page """
    return render_template('index.html')


@app.route("/api/reports/", methods=['GET', 'POST'])
def fetch():
    """ Reports are returned here """
    if request.method == 'GET':
        data = {}
        return Response(
            response=json.dumps(data), status=200, mimetype="application/json")
    else:
        print request


if __name__ == "__main__":
    app.debug = True
    app.run(
        host='0.0.0.0',
        port=5000
    )

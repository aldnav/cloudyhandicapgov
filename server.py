
""" MAIN APP SERVER """

import json
import dataset
from flask import Flask, render_template, Response
app = Flask(__name__)

db = dataset.connect('sqlite:///mydb.db')
table = db['tweets']


@app.route("/")
def index():
    """ Displays index page """
    return render_template('index.html')


@app.route("/api/reports/")
def fetch():
    """ Reports are returned here """
    data = []
    try:
        if len(table):
            for tweet in table.all():
                data.append({
                    'location': tweet['location'],
                    'status': tweet['status'],
                    'time': tweet['time'],
                    'name': tweet['name'],
                    'place': tweet['place']
                })
    except Exception, e:
        print e
    return Response(
        response=json.dumps(data), status=200, mimetype="application/json")


if __name__ == "__main__":
    app.debug = True
    app.run(
        host='0.0.0.0',
        port=5000
    )

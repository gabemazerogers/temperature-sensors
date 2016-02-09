from flask import Flask
from flask import render_template
import csv
import urllib.request

app = Flask(__name__)


    @app.route('/')
def hello_world():
    csv_data = csv.DictReader()
    return render_template("index.html", title='Sample page',data=csv_data)


if __name__ == '__main__':
    app.run()


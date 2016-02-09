from flask import Flask
from flask import render_template
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():
    with open('readings.csv') as csv_file:
        csv_data = csv.DictReader(csv_file.readlines())
    return render_template("index.html", title='Temperature Data',data=csv_data)

if __name__ == '__main__':
    app.run()




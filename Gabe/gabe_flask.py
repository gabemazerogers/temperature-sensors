from flask import Flask
from flask import render_template
import csv

with open('readings.csv') as csv_file:
	data = csv_file.readlines()
csv_data = csv.DictReader(data)
print data


app = Flask(__name__)

@app.route('/')
def display_CSV():
	with open('readings.csv') as csv_file:
		data = csv_file.readlines()
	csv_data = csv.DictReader(data)
	return render_template("index.html", title="Temperature Data", data=csv_data)

if __name__ == '__main__':
	app.run(debug=True)

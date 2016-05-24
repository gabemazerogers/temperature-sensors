import requests, json

url = "http://0.0.0.0:3000/api/Readings"
headers = {"Accept": "application/json"}

def insertData(location, temperature, date, time):
	payload = { "Location": "ERC", "Temperature": 75, "ReadingDate": "2016-05-23", "ReadingTime": "12:35" }
	res = requests.put(url, data=payload, headers=headers)
	print res

def getData():
	res = requests.get(url)
	print json.dumps(res.json(), sort_keys=True, indent=4)
	
getData()
# -*- coding: utf-8 -*-

# keep the above encoding message; DO NOT DELETE

# This file calls temper-poll and date; then, we put these unformatted strings
# to rawData.txt where we then parse appropriate values and create/append a .csv


import os, re, dateutil.parser, os.path, requests, json

url = "http://0.0.0.0:3000/api/Readings"
headers = {"Accept": "application/json"}

def insertData(location, temperature, date, time):
	payload = { "Location": location, "Temperature": temperature, "ReadingDate": date, "ReadingTime": time }
	res = requests.put(url, data=payload, headers=headers)

def getData():
	res = requests.get(url)
	print json.dumps(res.json(), sort_keys=True, indent=4)

location = "ERC"

# delete below line once we are ready to run on Rpi
os.system('echo $"Found 1 devices\nDevice #0: 22.5°C 72.5°F" > rawData.txt')

# the first call to temper-poll does not append because we want to wipe all
# previous data
#os.system('temper-poll > rawData.txt')
os.system('date >> rawData.txt')

rawData = open('rawData.txt', 'r')

lines = rawData.readlines() # initialized as list
temp_f = re.findall('\d+\.?\d*', lines[1])
# temp_f[2] = fahrenheit value

fullDate = dateutil.parser.parse(lines[2])
# fullDate = formatted dar+

exists = (os.path.isfile('formattedData.csv'))
logFile = open('formattedData.csv', 'w')
if(exists is False):
    logFile.write("Date,Temp,Place\n")
logFile.write(str(fullDate) + ", " + str(temp_f[2]) + ", " + location)
insertData(location, str(temp_f[2]), str(fullDate).split(" ")[0], str(fullDate).split(" ")[1])
getData()


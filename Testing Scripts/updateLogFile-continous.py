# -*- coding: utf-8 -*-

# keep the above encoding message; DO NOT DELETE

# This file calls temper-poll and date; then, we put these unformatted strings
# to rawData.txt where we then parse appropriate values and create/append a .csv


import os, re, dateutil.parser, os.path
from time import sleep

location = "ERC"

iter = 0.0

while True:
    tempTemp = 72.5 + iter
    # delete below line once we are ready to run on Rpi
    stringToWrite = "Found 1 devices\nDevice #0: 22.5°C" + str(tempTemp) + "°F"
    os.system('echo $"'+stringToWrite+'" > rawData.txt')

    # the first call to temper-poll does not append because we want to wipe all
    # previous data
    #os.system('temper-poll > rawData.txt')
    os.system('date >> rawData.txt')

    rawData = open('rawData.txt', 'r')

    lines = rawData.readlines() # initialized as list
    temp_f = re.findall('\d+\.?\d*', lines[1])
    # temp_f[2] = fahrenheit value

    fullDate = dateutil.parser.parse(lines[2])
    # fullDate = formatted date

    exists = (os.path.isfile('formattedData.csv'))
    logFile = open('formattedData.csv', 'a')
    if(exists is False):
        logFile.write("Date,Temp,Place\n")
    logFile.write(str(fullDate) + ", " + str(temp_f[2]) + ", " + location + "\n")

    iter = iter + 0.1
    if iter > 3.0:
        break

    sleep(5) # sleep 5 seconds


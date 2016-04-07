import pysftp, re

"""sftp.py: Opens a connection with ieng6 (or whatever server) and reads the output of the temper poll command and locates the farenheit temperature using regex"""

serverName = 'acsweb.ucsd.edu'
username = "ewb" # REPLACE WITH YOURS
password = "" # REPLACE WITH YOURS

filePath = '~/Temperature_Project_2016/rawData.txt'
# rawData.txt holds unformatted temper-poll results, the date, and newline char

with pysftp.Connection(serverName,username=username,password=password, port=22) as sftp:
	sftp.get(filePath, '')

# TODO

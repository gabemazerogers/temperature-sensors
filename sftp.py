import pysftp, re

"""sftp.py: Opens a connection with ieng6 (or whatever server) and reads the output of the temper poll command and locates the farenheit temperature using regex"""

serverName = 'ieng6.ucsd.edu'
username = "" # REPLACE WITH YOURS
password = "" # REPLACE WITH YOURS
filePath = ''
with pysftp.Connection(serverName,username=username,password=password, port=22) as sftp:
	sftp.get(filePath, '')

tempFile = open(filePath, 'r')

lines = tempFile.readlines() # initialized as list
temp_f = re.findall('\d+\.?\d*', lines[1])
print temp_f[2]
fullDate = dateutil.parser.parse(lines[2])
print fullDate

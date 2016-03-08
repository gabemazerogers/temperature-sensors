import pysftp
serverName = 'ieng6.ucsd.edu'
username = "" # REPLACE WITH YOURS
password = "" # REPLACE WITH YOURS
filePath = 'python/temp.txt'
with pysftp.Connection(serverName,username=username,password=password, port=22) as sftp:
	sftp.get(, '')
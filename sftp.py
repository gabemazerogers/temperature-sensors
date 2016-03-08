import pysftp, re
serverName = 'ieng6.ucsd.edu'
username = "" # REPLACE WITH YOURS
password = "" # REPLACE WITH YOURS
filePath = ''
with pysftp.Connection(serverName,username=username,password=password, port=22) as sftp:
	sftp.get(filePath, '')

tempFile = open(filePath, 'r')
lines = tempFile.readlines()
lines = ''.join(lines)
print lines
temp_f = re.findall('\d+\.?\d*', lines)
print temp_f[3]

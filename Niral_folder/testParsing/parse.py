import dateutil.parser

f = open("sampleOutput.txt", "r")

f.readline()
degreeline = f.readline() #degrees line
# do something
dateLine = f.readline()
fullDate = dateutil.parser.parse(dateLine)
print fullDate


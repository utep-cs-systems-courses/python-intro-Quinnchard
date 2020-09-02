import sys
import string

inputfname = sys.argv[1]
outputfname = sys.argv[2]

with open(inputfname, 'r') as inputFile:
    d = dict()
    for line in inputFile:
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans("", "", string.punctuation))
        words = line.split(" ")
        for word in words:
            if word in d:
                d[word] = d[word] + 1 
            else:
                d[word] = 1 
                
with open(outputfname, 'w') as outputFile:
    for key in list(sorted(d)):
        outputFile.write('%s : %s\n' % (key, d[key]))
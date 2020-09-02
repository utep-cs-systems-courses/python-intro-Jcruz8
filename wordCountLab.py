import sys
f = sys.argv[1]
o = sys.argv[2]
wordsDict = dict()

#opens file to read
with open(f,"r") as f:
    for line in f:
        line = line.lower()
        for word in line.split():
            if word in wordsDict:
                wordsDict[word] += 1
            else:
                wordsDict[word] = 1
f.close()
sortedDict = sorted(wordsDict.items(), key = lambda x: x[1], reverse = True)

#opens file to write
with open(o, "w") as o:
    for i in sortedDict:
        o.write(i[0] + " " + str(i[1]) + "\n")
o.close()

f = open("testfile.txt", "r")
#o =open("output.txt", "w").close()

wordsDict = dict()

#print(f.read())
for line in f:
    line = line.lower()
    for word in line.split():
        if word in wordsDict:
            wordsDict[word] += 1
        else:
            wordsDict[word] = 1
#sortedWordsDict = {}
#sortedWordsDict = sorted(wordsDict, reverse = True)
o = open("output.txt", "w")
#o.write(str(wordsDict))
#o.close()
#for key in sorted(wordsDict.items(), reverse = True):
#    o.write(key + " " + str(wordsDict[key]) + "\n")
sortedDict = sorted(wordsDict.items(), key = lambda x: x[1], reverse = True)
for i in sortedDict:
    o.write(i[0] + " " + str(i[1]) + "\n")
o.close()
f.close()

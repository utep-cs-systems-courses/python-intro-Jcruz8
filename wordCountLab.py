f = open("testfile.txt", "r")
o =open("output.txt", "w").close()

wordsDict = {}

#print(f.read())
for line in f:
    for word in line.split():
        if word in wordsDict:
            wordsDict[word] += 1
        else:
            wordsDict[word] = 1
#sortedWordsDict = {}
#sortedWordsDict = sorted(wordsDict, reverse = True)
o = open("output.txt", "a")
o.write(str(wordsDict))
o.close()
f.close()

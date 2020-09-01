f = open("testfile.txt", "r")
o =open("output.txt", "w").close()

words = {}

#print(f.read())
for line in f:
    for word in line.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    o = open("output.txt", "a")
    o.write(str(words))
    o.close()
            
        #print(word)
        
f.close()

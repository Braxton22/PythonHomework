file = open("text.txt", "r")
file2 = file.readlines()

listofwords = []

for line in file2:
    listofwords.append(line.split())

worddictionary = {}
currentwordcount = 0

for sentence in listofwords:
    for word in sentence:
        wordupper = word.upper()
        if wordupper not in worddictionary:
            worddictionary[wordupper] = 1
        else:
            currentwordcount = worddictionary[wordupper]
            newcurrentwordcount = currentwordcount + 1
            worddictionary[wordupper] = newcurrentwordcount

print(worddictionary)

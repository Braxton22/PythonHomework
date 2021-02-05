# Open File
file = open("text.txt", "r")
file2 = file.readlines()

# Create list to store lines
listofwords = []

# for each sentence in the file, put it into the listofwords list
for line in file2:
    listofwords.append(line.split())

# Create Dictionary
worddictionary = {}
# Create variable to count the words
currentwordcount = 0

# Iteratae through sentences
for sentence in listofwords:
    # Iterate through words
    for word in sentence:
        # Standardize to upper case
        wordupper = word.upper()
        # If the word isn't in the dictionary, put it in there and set its value to 1
        if wordupper not in worddictionary:
            worddictionary[wordupper] = 1
        # If the word is in the dictionary, add one to its value
        else:
            currentwordcount = worddictionary[wordupper]
            newcurrentwordcount = currentwordcount + 1
            worddictionary[wordupper] = newcurrentwordcount

# print the output
print(worddictionary)

# close file
file.close()

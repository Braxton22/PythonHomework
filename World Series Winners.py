file = open("WorldSeriesWinners.txt", "r")
filelines = file.readlines()
strippedfile = []
for team in filelines:
    strippedfile.append(team.rstrip("\n"))

teamdictionary = {}
yearwinner = {}
yearinteger = 1903
numberofwins = 0
firstyear = yearinteger
lastyear = 0

for team in strippedfile:
    if yearinteger == 1904 or yearinteger == 1994:
        yearwinner[yearinteger] = "No World Series This Year"
    else:
        yearwinner[yearinteger] = team
    yearinteger += 1

    if team not in teamdictionary:
        teamdictionary[team] = 1
    else:
        numberofwins = teamdictionary[team]
        newnumberofwins = numberofwins + 1
        teamdictionary[team] = newnumberofwins

lastyear = yearinteger - 1

print(firstyear)
print(lastyear)


Userinput = int(input("PLease enter a value between 1903 and 2006: "))

if Userinput not in range(firstyear, lastyear + 1):
    print("Error: Please Enter A Value Between", firstyear, "and", lastyear)
elif Userinput == 1904 or Userinput == 1994:
    print("There was not a World Series in that year")
else:
    print(
        "The",
        yearwinner[Userinput],
        "won in",
        Userinput,
        "and they have won the world series",
        teamdictionary[yearwinner[Userinput]],
        "times in total.",
    )

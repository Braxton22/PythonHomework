# Open File
file = open("WorldSeriesWinners.txt", "r")
# Read lines in the file
filelines = file.readlines()
# Create a list for the stripped lines
strippedfile = []
# Iterate through filelines variable and append elements into the list stripped of \n
for team in filelines:
    strippedfile.append(team.rstrip("\n"))

# Set the stage - create dictionaries and variables
teamdictionary = {}
yearwinner = {}
yearinteger = 1903
numberofwins = 0
firstyear = yearinteger
lastyear = 0

# Iterate through teams in the stripped file
for team in strippedfile:
    # if the year is 1904 or 1994, when the world series wasn't played, store its value as no world series this year
    if yearinteger == 1904 or yearinteger == 1994:
        yearwinner[yearinteger] = "No World Series This Year"
    # if the year is any other year, set the value to the team
    else:
        yearwinner[yearinteger] = team
    # accumulate
    yearinteger += 1

    # If the team isn't in the team dictionary yet, put it in there and set its value to 1
    if team not in teamdictionary:
        teamdictionary[team] = 1
    # if it is in there, add one to its value
    else:
        numberofwins = teamdictionary[team]
        newnumberofwins = numberofwins + 1
        teamdictionary[team] = newnumberofwins

# preparation for print statements - the .txt file only contained world series from 1903 to 2006, so I used a variable rather than hardcoding those values
lastyear = yearinteger - 1

# Ask user for a year
Userinput = int(input("Please enter a value between 1903 and 2006: "))

# If the year isn't between the first and last year, error out
if Userinput not in range(firstyear, lastyear + 1):
    print("Error: Please Enter A Value Between", firstyear, "and", lastyear)
# If the year is 1904 or 1994, tell the user there is not a world series in that year
elif Userinput == 1904 or Userinput == 1994:
    print("There was not a World Series in that year")
# Print the team and how many times they have won for the user's inputted year
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

# close file
file.close()

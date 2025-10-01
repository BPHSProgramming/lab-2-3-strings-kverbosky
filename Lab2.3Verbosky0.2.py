#print("Kuon Verbosky", "Period 8", "9/23/25", sep = "\n") 

# Task 1
print("Task #1")
fullName = input("What is your full name?\t")
firstName = fullName[:fullName.find(" ", 0)]
lastName = fullName[fullName.find(" ", 0)+1:]

print(firstName.title(), end=" ")
print(lastName.title()) 
print(firstName[0:1].lower() + firstName[1:].upper() +\
", " + lastName[0:1].lower() + lastName[1:].upper()) 
print()

# Task 2
print("Task #2")
phrase = "Once you start down the dark path, forever will it dominate your destiny."
phraseUppered = phrase.upper()
phraseEncrypted = phraseUppered.replace("A","1").replace("E","2").replace("I","3")
phraseEncrypted = phraseEncrypted.replace("O","4").replace("U","5")
print(phraseEncrypted)
print()

# Task 3
print("Task #3")
length = len(phrase)
phraseFirst = phrase[0:int(length/3)]
phraseSecond = phrase[int(length/3):int(length/3*2)]
phraseThird = phrase[int(length/3*2):length-1]
print(phraseSecond + phraseFirst + phraseThird)
print()

# Task 4
print("Task #4")
fiveDNumber = input("Enter a 5 digit number:\t")
digit1 = int(fiveDNumber[0:int(len(fiveDNumber)/5)])
digit2 = int(fiveDNumber[int(len(fiveDNumber)/5):int(len(fiveDNumber)/5*2)])
digit3 = int(fiveDNumber[int(len(fiveDNumber)/5*2):int(len(fiveDNumber)/5*3)])
digit4 = int(fiveDNumber[int(len(fiveDNumber)/5*3):int(len(fiveDNumber)/5*4)])
digit5 = int(fiveDNumber[int(len(fiveDNumber)/5*4):int(len(fiveDNumber))])
print(digit1, "+", digit2, "+", digit3, "+", digit4, "+", digit5, "=", +\
digit1+digit2+digit3+digit4+digit5)
print()

# Task 5
print("Task #5")
otherPhrase = "Why, you stuck-up half-witted scruffy-looking nerf herder"
frontToBack = otherPhrase[0:len(otherPhrase):2]
backToFront = otherPhrase[-len(otherPhrase):len(otherPhrase):2]
print(frontToBack, backToFront, sep="\n")
print()

# Task 6
print("Task #6")

from datetime import date
today = date.today()
today = today.strftime("%Y,%B,%d")
print(f"The date today is {today}")
commaOne = today.find(",",0)
commaTwo = today.find(",",commaOne+1)

month = today[commaOne+1:commaTwo]
day = today[commaTwo+1:]
year = today[0:commaOne]
print("Today is day", day, "of", month, year, end=".")
print()

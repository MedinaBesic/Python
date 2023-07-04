# A For loop moves through a given range of numbers 
#If only one number is provided it will loop from 0 to that number
for x in range(10):
    print(x)
#this should print numbers 1-9, starting with 0


# If two numbers are provided, then a For loop will loop from the first number up until it reaches the second number
for x in range(20, 30):
    print(x)
#this should print numbers 20-29

#If a list is provided, then the For loop will loop through each element within the list 
words= [ "Peanut", "Butter", "Jelly", "Time", "Is", "Now" ]
for word in words:
    print(word)
#this should print each word individually: Peanut
#this should print each word individually: Butter

# A While loop will continue to loop through the code contained within it until some condition is met 
x = "Yes"
while x == "Yes":
    print("Whee! Merry-Go-Rounds are great!")
    x=input("Would you like to go on the Merry-Go-Round again? ")
#This should keep printing the last two lines of code (last two print statements) unless anything other than "Yes" is input
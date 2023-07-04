# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

n=len(candy_list)

for i in range(n):
    print(i, candy_list[i])

#the list used to store all of the candies selected 
candy_cart = []

#Create a version of the code that allows a user to select
#as much candy as they want until they say they do not want any more.
x = "Yes"
while x == "Yes":
    user_input=int(input("Please select a candy from the candy store from 0 to 8. "))
    #store the user_input each time a selection is made
    selection = candy_list[user_input]
    # The list used to store all of the candies selected inside of
    candy_cart.append(selection)
    x=input("Would you like to make another selection? Yes or no? ")

# Print out what the user selected to take home
print("You brought home with you ")
for candy in candy_cart:
    print(candy)

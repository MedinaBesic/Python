# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

n=len(candy_list)

for i in range(n):
    print(i, candy_list[i])

candy_cart = []

# The amount of candy the user will be allowed to choose
allowance = 5


for j in range(allowance):
    user_input=int(input("Please select a candy from the candy store from 0 to 8. "))
    #store the user_input each time a selection is made in a variable
    selection = candy_list[user_input]
    # The list used to store all of the candies selected inside of
    candy_cart.append(selection)

# Print out options
print(candy_cart)
# # The list of candies to print to the screen
# candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# # The amount of candy the user will be allowed to choose
# allowance = 5

# n=len(candy_list)

# for i in range(n):
#     print(i, candy_list[i])  #index, item
# # The list used to store all of the candies selected inside of
# candy_cart = []

# for j in range(allowance):
#     user_input = int(input("What number of candy do you want? 0 to 8"))

#     candy = candy_list[user_input]


# candy_cart.append(candy)
# #Can use this instead of creating a new variable candy candy_cart.append(candy_list[user_input])

# print(candy_cart)

# Print out options

import csv
import time

# #This next function is how you open a file 
# #if it's in a different directory that you don't have open in your terminal, then you need to give the full path 
#  #another way to open it : csvfile = open('myfile.csv')
with open('myfile.csv') as csvfile: 
    #this is how you read the entire file to see the content of the file 
    csvreader=csv.reader(csvfile, delimiter= ',')
    print(csvreader)

    #if you want to read every row
    if row in csvreader:
        print(row)   
    
    for row in cvsreader:
        time.sleep(2)
        print(row)



#a is append 
# #w means write, this is the mode, to write only 
# with open('myfile.csv', a) as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter = ',')

#     csvwriter.writerow(['Mary', '54', '250000', '', ''])

#     print('writing done!')






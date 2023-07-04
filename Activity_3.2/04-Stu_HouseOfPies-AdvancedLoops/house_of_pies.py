print("Welcome to the House of Pies! Here are our pies: ")

#Create a list of pies
pies=['Pecan', 'Apple Crisp', 'Bean', 'Banoffee', 'Black Bun', 'Blueberry', 'Buko', 'Burek', 'Tamale', 'Steak']

#Display the options with the index numbers
n=len(pies)

for i in range(n):
    print(i, pies[i])

piesselection= []

#Then, prompt the user to enter the number for the pie they would like to order.
#user_input=int(input("What pie would you like to order? Enter a number from 0 to 9. "))
#order=pies[user_input]

#Immediately follow up their order with `Great! We'll have that <PIE NAME> right out for you`,
#print("Great! We'll have that {} right out for you.".format(order))

#and then ask if they would like to make another order. If so, repeat the process.
x= "Yes"
while x == 'Yes':
    user_input=int(input("What pie would you like to order? Enter a number from 0 to 9. "))
    order=pies[user_input]
    print("Great! We'll have that {} right out for you.".format(order))
    piesselection.append(order)
    x=input("Would you like to make another order? ")
else: 
    print("You ordered a total of {} pies".format(len(piesselection)))






# @TODO: Your code here
fish= "halibut"

#loop thru each letter in the string 
#and push to an array
#aka we are creating a list for each letter in the value of the variable fish
letters=[]
for letter in fish:
    letters.append(letter)

print(letters)

#List comprehensions provide concise syntax for creating lists
#object and then the for loop
letters = [letter for letter in fish]

print(letters)

#We can manipulate each element as we go
capital_letters=[]
for letter in fish: 
    capital_letters.append(letter.upper())

print(capital_letters)

#list comprehensions from the above
capital_letters = [letter.upper() for letter in fish]

print(capital_letters)

#We can also add conditional logic (if statements) to a list comprehension
july_temperatures = [ 87, 85, 92, 79, 106]
hot_days = []
for temperature in july_temperatures:
    if temperature > 90:
        hot_days.append(temperature)

print(hot_days)

#List comprehension with conditional 
hot_days = [temperature for temperature in july_temperatures if temperature > 90]

#what you are looking for, then if/else 
#hot_days= [temperature if temperature > 90 else 0 for temperature in july_temperatures]

#you can do boolean values with the code above
hot_days= ["YES" if temperature > 90 else "NO" for temperature in july_temperatures]


print(hot_days)
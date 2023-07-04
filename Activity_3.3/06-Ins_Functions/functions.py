#Basic Definition
#def name(parameters):
    #code goes here
    #return



#Simple Funtion with no parameters
def show():
    print(f"Hi!")


#you use parantheses to run the code in a function
show()

#Simple function with one parameter
def show(message):
    print(message)


#Think of the parameter 'message' as a variable
#You assign the string "Hello, World" when you call the function
#this is like saying 'message = "Hello, World!"'
show("Hello, World!")


#Functions can have more than one parameter
def make_quesadilla(protein, topping):
    quesadilla= f'Here is a {protein} quesadilla with {topping}'
    print(quesadilla)


#supply the arguments (values) when calling the function 
make_quesadilla("beef", "guacamole")
make_quesadilla("chicken", "salsa")

#We can also specify default values for parameters
def make_quesadilla(protein, topping="sour cream"):
    quesadilla = f'Here is a {protein} quesadulla with {topping}'
    print(quesadilla)

#Make a quesadilla using the default topping
make_quesadilla("chicken")

#Make a quesadilla with a new topping 
make_quesadilla("beef", "guacamole")


#functions can return a value 
def square(number):
    return number * number

#you can save the value that is returned 
squared = square(2)
print(squared)

#you can also print the return value of a function
print(square(2))
print(square(3))

#This following line would return error because it's a string
#print(square("abc"))

#a float value will work
print(square(2.1))



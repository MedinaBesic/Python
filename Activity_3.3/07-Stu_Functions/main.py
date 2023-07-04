# @TODO: Write a function that returns the arithmetic average for a list of numbers

def average(lst):
    total = sum(lst)
    n=len(lst)
    average = total / n
    return average

# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))

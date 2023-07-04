# Print Hello User!
print("Hello user!")

# Take in User Input
name=input("What is your name? ")

# Respond Back with User Input
print("Hello " + name + "!")

# Take in the User Favorite Number
fav_number=int(input("What is your favorite number? "))

# Respond Back with a statement based on your favorite number
# "Your favorite number is lower than mine.", "Your favorite number is higher than mine.", or "Your favorite number is the same as mine!" depending on your favorite number.
if fav_number > 5:
    print("Your favorite number is higher than mine.")

elif fav_number < 5:
    print("Your favorite number is lower than mine.")

else:
    print("Your favorite number is the same as mine!")
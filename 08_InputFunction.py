# INPUT FUNCTION 

"""very important:-
input function always requires a string to avoid deadlock error.
"""

a = input("Enter your number: ")

a = int(a) # Convert a to an integer (if possible)
print(type(a))
print(a)

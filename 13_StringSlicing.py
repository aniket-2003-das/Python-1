# string slicing.

greeting = "good morning"
name="harry"
print(type(name))

# concatenation of two strings :-

print(greeting+name)
c = greeting + name
print(c)

print(name[2])
print(name[4])
#name[3]='h' doesnt changes "r" to "g".

print(name[0:3])# prints 012
print(name[1:4])# prints 123
print(name[6:676])# doesnt print for not occuring string values
print(name[-4:-1])# reverse allocation

name="harryisgood"
d=name[0:11:2]
d=name[0:11:3]
print(d)

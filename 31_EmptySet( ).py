# the system will create an empty Dictionary not an empty Set.
a = {}
print(type(a))

# this system creates an empty set
b = set()
print(type(b))
b.add(4)
b.add(5)
b.add(5)
b.add(5)


print(b)
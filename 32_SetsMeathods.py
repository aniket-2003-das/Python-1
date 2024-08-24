# Sets Meathods:-

b = set()
# add values to null set
b.add(4)
b.add(5)
# b.add([4,5,6]) #list cant be added as its not hashable contents can be changed
b.add((4,5,6)) #tupple can be addded
# b.add({4:5})  #dictionary cant be added as its not hashable contents can be changed

print(b)

print(len(b)) # prints the length of this set
b.remove(5)
# b.remove(15) throws an error as 15 is not in set 

print(b)

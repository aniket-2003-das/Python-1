# use open function to read the content of a file 

# f = open('sample.txt', 'r')
f = open('72_sample.txt') #by default the code is r

# data = f.read()
data = f.read(11)# reads only 11 charectars

print(data)
f.close()
# no need to close file with the with statement. 
with open('75_another.txt', "r") as f:
# if by chance u open file in w or a mode the content of the file
# gets deleted and non readable error is shown. 
    a = f.read()
print(a)
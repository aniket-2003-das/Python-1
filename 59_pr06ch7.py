num = int(input("enter the number:\n"))
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
print(f"the facorial of this number is {factorial}")
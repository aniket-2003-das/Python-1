class Employee:
    company = "Google"
    salary = 150 # class attribute

harry = Employee()
rajni = Employee()

# creating instance attribute salary for both the objects
harry.salary = 45
# rajni.salary = 400
harry.salary = 300 # overwrites salary.

print(harry.salary)
print(rajni.salary)

# print(rajni.address) "throws an error as address attribute is not present in the instance" 


class Employee:
    company = "google"

    def showdetails(self):
        print("this is an employee")

class Programmer(Employee):
    language = "python"
    company = "MASA"
    def getName(self):
        print(f"the language is {self.language}")
    
    def showdetails(self):
        print("this is an programmer")

e = Employee()
e.showdetails()
p = Programmer
p.showdetails
print(p.company)
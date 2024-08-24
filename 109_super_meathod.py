class person:
    country = "india"
    
    def __init__(self):
        print("initializing person...\n")
    
    def takeBreath(self):
        print("i am breathing")
    
class Employee(person):
    company = "honda"

    def __init__(self):
        super().__init__()
        print("initializing employee...\n")
    
    def getSalary(self):
        print(f"the salary is {self.Salary}")

    def takeBreath(self):
        super().takeBreath()
        print("i am employee so i am luckyly breathing")

class Programmer(Employee,person):
    company = "fiverr"
    
    def __init__(self):
        super().__init__()
        print("initializing programmer...\n")

    def getSalary(self):
        print("no salary to programmers")
    
    def takeBreath(self): # if dont have meathod then aquires nearest meathod (from Employee)
        super().takeBreath()
        print("i am programmer so i am luckyly breathing ++")

p = person()
# p.takeBreath()

e = Employee()
# e.takeBreath()

pr = Programmer()
# pr.takeBreath()


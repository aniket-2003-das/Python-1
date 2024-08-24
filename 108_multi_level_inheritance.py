class person:
    country = "india"
    def takeBreath(self):
        print("i am breathing")
    
class Employee:
    company = "honda"

    def getSalary(self):
        print(f"the salary is {self.Salary}")

    def takeBreath(self):
        print("i am employee so i am luckyly breathing")

class Programmer(Employee,person):
    company = "fiverr"

    def getSalary(self):
        print("no salary to programmers")
    
    def takeBreath(self): # if dont have meathod then aquires nearest meathod (from Employee)
        print("i am programmer so i am luckyly breathing ++")

p = person()
p.takeBreath()
e = Employee()
e.takeBreath()
pr = Programmer()
pr.takeBreath()

print(p.country)
print(pr.country)
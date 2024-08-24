class Employee:
    company = "bharat gas"
    salary = 4500
    bonus = 500
    # totalSalary = 5000
    # or 
    @property
    def totalSalary(self):
        return self.salary + self.bonus
    
    @totalSalary.setter
    def totalSalary(self,val):
        self.bonus = val - self.salary

e = Employee()
e.totalSalary = 5800
print(e.totalSalary)
print(e.bonus)


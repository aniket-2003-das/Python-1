class Employee:
    company = "visa"
    eCode = 120

class Freelancer:
    company = "fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Freelancer,Employee):
    name = "rohit"

p = Programmer()
p.upgradeLevel()
print(p.company)

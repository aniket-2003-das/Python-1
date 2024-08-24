class Employee:
    company  = "camel"
    salary = 100
    lacation = 'delhi'

    def changeSalary(self, sal):
        self.__class__.salary = sal
    # or 
    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(400)
print(e.salary)
print(Employee.salary)

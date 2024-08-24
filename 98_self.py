class Employee:
    company = "Google"
    def getSalary(self,signature):
        print(f"salary for this employee working in {self.company} is {self.Salary}\n{signature}")
    
    @staticmethod
    def greet():
        print("good morning, sir")

    @staticmethod
    def time():
        print("the time is 9 AM in the morning.")


harry = Employee()
harry.Salary = 100000
harry.getSalary("thanks")  # Employee.getSalary(harry)
harry.greet() # Employee.greet()
harry.time()
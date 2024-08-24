class Employee:
    company = "Google"

    def __init__(self, name, Salary, Subunit):
        self.name = name
        self.Salary = Salary
        self.Subunit = Subunit
        print("employee is created")

    def getDetails(self):
        print(f"the name of the employee is {self.name}") 
        print(f"the Salary of the employee is {self.Salary}")  
        print(f"the Subunit of the employee is {self.Subunit}")  

    def getSalary(self,signature):
        print(f"salary for this employee working in {self.company} is {self.Salary}\n{signature}")
    
    @staticmethod
    def greet():
        print("good morning, sir")

    @staticmethod
    def time():
        print("the time is 9 AM in the morning.")
        
harry = Employee("harry", 100, "youtube")
# harry = Employee() this throws an error of 3 missing reqd arguements 
harry.getDetails()
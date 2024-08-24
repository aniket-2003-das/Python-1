class Calculator:
    def __init__(self, num) :
        self.number = num
    
    def square(self):
        print(f"the value of {self.number} is {self.number**2}")

    def squareRoot(self):
           print(f"the value of {self.number} is {self.number**0.5}")


    def cube(self):
           print(f"the value of {self.number} is {self.number**3}")

    @staticmethod
    def greet():
        print("hello welcome to the best calculator")

a = Calculator(3)
a.greet()

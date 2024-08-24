class Programmer:
    company = "microsoft"
    
    def __init__(self, name, product) :
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"the name oftthe company is {self.company}.\n The name of the programmer is {self.name} \n and product is {self.product}.")

harry = Programmer("harry", "skype")
alka = Programmer("alka", "github")
harry.getInfo()

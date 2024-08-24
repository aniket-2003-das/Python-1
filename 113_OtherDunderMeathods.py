# Other Dunder Meathods
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("lets add")
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("lets multiply")
        return self.num * num2.num
    
    def __str__(self):
        return f"decimal number :\n {self.num} "
    
    def __len__(self):
        print("the len is :")
        return 1

n = Number(9)
print(n)
print(len(n))
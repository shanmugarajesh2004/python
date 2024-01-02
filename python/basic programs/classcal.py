# class calculator:
#     def add(self,a,b):
#         print(a+b)

# obj1 = calculator()
# obj1.add(10,20)        

# using __init__

class calculator():
    def __init__(self,a,b) -> None:
        self.sum1 = a
        self.sum2 = b
    def add(self):
        print(self.sum1+self.sum2)

    def sub(self):
        print(self.sum1-self.sum2)    
obj1 = calculator(10,20)
obj1.add()  

obj2 = calculator(20,10)
obj2.sub()


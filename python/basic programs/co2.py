class laptop:
    def __init__(self) -> None:
         self.price = 2000
         self.ram = "8"
    def display(self):
        print("price is :",self.price)
        print("ram is :",self.ram)

dell = laptop()
hp = laptop()

dell.price = 10000
dell.ram = 16

dell.display()
hp.display()
class company():
    def __init__(self) -> None:
        self.__company = "google"  #----------> here __ symbol represent encapsulation were it can be only access in class only
        pass
    def display(self):
        print(self.__company)
        pass
    pass

b1 = company()
b1.display()

print()

class a():
    def __init__(self) -> None:
        print("A")

class b(a):
    def __init__(self):
        super().__init__() #--------------> call parent class construtor
        print("B")

class c(b,a):  #---------------------------> multiple inheritance
    def __init__(self) -> None:
        super().__init__() #---------------->go to b class in b have super for a so print A and than B lastly come to C
        print("C")


obj =  c()              
class teacher:
    def __init__(self,v1,v2) -> None:
        self.name = v1
        self.registerno = v2
    def display(self):
        print(self.name)
        print(self.registerno)
t1 = teacher("kerthana","696969")
t2 = teacher("vinothini","999666")


t1.display()
t2.display()

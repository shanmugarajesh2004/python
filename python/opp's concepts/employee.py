class employee():
    def __init__(self,name,salary) -> None:
        self.name = name
        self.salary = salary
        pass
    pass
class manager(employee):
    def __init__(self,department,name,salary) -> None:
        super().__init__(name,salary)
        self.department = department
        pass
    def display(self):
        print(self.name,self.department,self.salary)
        pass
    pass

obj = manager("CSE","shamuga","100000")
obj.display()
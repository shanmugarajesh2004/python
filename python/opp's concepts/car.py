class vehical():
    def start(self):
        print("vehical started")
        pass
    pass
class car(vehical):
    def start(self):
        print("car started")
        pass
    pass

obj1 = vehical()
obj1.start()
obj2 = car()
obj2.start()
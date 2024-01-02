class dad():
    def money(self):
        print("dad money")

class land():
    def importantland(self):
        print("impotent land")        

class son1(dad):
    pass

class son2(dad,land):                    # if more than one class inherite a one class means it is hirarica inhertance
        pass
       
                                         # if single,multiple,multilevel and hirarica infertance all are hybrid inheritance 
class son3(dad):
    pass

shanmuga = son2()
shanmuga.money()
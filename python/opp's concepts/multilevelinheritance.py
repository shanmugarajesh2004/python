class grandpa():
    def phone(self):
        print("granpa phone")

class dad(grandpa):                      # inherit granpa to dad
    def money(self):                      
        print("dad money")

class son(dad):                          # inherit dad to son so we can ascces dad mony and grandpa phone multilevel inhertance
    def laptop(self):
        print("son lotop")

shanmuga = son()
shanmuga.money()
shanmuga.phone()
print()

raj = dad()











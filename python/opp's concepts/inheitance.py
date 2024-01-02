class dad():
    def phone(self):
        print("dad's phone")

class mom():
    def sweet(self):
        print("palkova sweet")        

class son(dad,mom):   #inherit dad and mom class in son
    def laptop(self):
        print("son's laptop")

shanmuga = son()
shanmuga.phone()   #calling class dad phone
shanmuga.laptop()
shanmuga.sweet()        
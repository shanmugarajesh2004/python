class goa:
    name = ""
    drink = ""
    def party(self):
        print("Let's party......!")
    def beach(self):
        print("Enjoy in beach and sunset")
shanmuga = goa()
rajesh = goa()



shanmuga.name = "shanmuga"
shanmuga.drink = "No"
rajesh.name = "rajesh"
rajesh.drink = "Yes"


print("Name :",shanmuga.name)
print("Drink :",shanmuga.drink)
shanmuga.beach()
print("*********************")
print("Name :",rajesh.name)
print("Drink :",rajesh.drink)
rajesh.party()




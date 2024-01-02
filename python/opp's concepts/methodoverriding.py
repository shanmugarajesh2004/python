class animal():
    def sound(self):
        print("Anima make soun")
class dog(animal):
    def sound(self):
        print("dog bark") 
class bird(animal):
    def sound(self):
        print("bird sing") 
               

d1 = dog()
d1.sound()

d2 = animal()
d2.sound()

d3 = bird()
d3.sound()

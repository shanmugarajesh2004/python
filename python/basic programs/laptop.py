class laptop:
    price = ""
    Processor = ""
    Ram = ""

HP = laptop()
DELL = laptop()
LENOVO = laptop()

h1 = HP.price= "40,000"
h2 = HP.Processor="intel CORE i3"
h3 = HP.Ram = "8 GB RAM"

d1 = DELL.price= "60,000"
d2 = DELL.Processor="intel CORE i5"
d3 = DELL.Ram = "16 GB RAM"

l1 = HP.price= "100,000"
l2 = HP.Processor="intel CORE i7"
l3 = HP.Ram = "32 GB RAM"

print("HP Laptop spcification")
print(h1)
print(h2)
print(h3)

print()
print("DELL Laptop spcification")
print(d1)
print(d2)
print(d3)

print()
print("Lenovo Laptop spcification")
print(l1)
print(l2)
print(l3)
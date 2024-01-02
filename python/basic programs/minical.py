a = int(input("A :"))
b = int(input("B :"))

opration = input("Add/sub/mul/div/modul :")

if(opration=="Add"):
    print(a + b)
elif(opration=="sub"):
    print(a - b)
elif(opration=="mul"):
    print(a * b)
elif(opration=="div"):
    print(a / b)
elif(opration=="modul"):
    print(a % b)
else:
    print("invalid")                          
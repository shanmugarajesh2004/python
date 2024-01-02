def passorfail(num):
    if(num<35):
        print("Fail")
    elif(num>100):
        print("Enter a valid mark")    
    else:
        print("Pass")

a = int(input("Enter ypur Mark :"))

passorfail(a)
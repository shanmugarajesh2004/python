salary = int(input("Enter your salary :"))
age = int(input("enter your Age:"))

if(salary >=20000 or age <=25):
    print("You are eligible for lone")
    lone=int(input("Enter the required lone amount :"))
    if(lone<=50000):
        print("you are eligible for lone")
    else:
        print("Maximum lone amount is : 50000")   
          
else:
    print("you are not eligibile for lone")    

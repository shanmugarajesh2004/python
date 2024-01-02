# count = 0

# for i in range(1,101):
#     if(i%3==0 and i%5==0):
#         count=count+1
# print(count)         


# a = 23
# b = 13

# print(a//b)
# print(a/b)

# sum=0
# for i in range(1,5+1):
  
#         sum=sum+i
# print(sum)    


a=[]
print("Enter the 10 numbers")

for i in range(10):
    sum = int(input("Enter the number"+str(i+1)+":"))
    a.append(sum)
print(a)

b=0
for i in a:
    b=b+i
print(b//10)    


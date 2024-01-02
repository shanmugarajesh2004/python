score = int(input("Score :"))

if(score < 35):
    print("RA")
elif(score >= 35 and score < 50):
    print("C Grade")
elif(score >= 50 and score < 60):
    print("B Grade")
elif(score >= 60 and score < 70):
    print("B+ Grade")
elif(score >= 70 and score < 80):
    print("A Grade")
elif(score >= 80 and score < 90):
    print("A+ Grade") 
elif(score >= 90 and score <= 100):
    print("O Grade")               
else:
    print("invalid")            
f = open("frutis.txt","a") #------------->"a" writing and reading into a file 
f.write("watermalon\n") #----------------->add new element to the file
f.write("bannan\n")

f.close() #-------------------------------> if we open a file means we have to close the file


f = open("frutis.txt","r") #------------->"r" is for reading a file  
print(f.read())



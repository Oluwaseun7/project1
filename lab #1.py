#Akinnusotu_lab01

#Question 2.2 Half Pyramid

for k in range(1,6):#A variable in k for the range from 1-6
    print("#"*k)#The user multiply the variable k for my string "#"

#Question 3.3 Circle

height= int(input("what is the variable number?"))#the user wants a variable  
for k in range(0, height+ 1):#takes the height and adds 1
    if(k==0) or (k== height):#wants to know if k equals 0 or the height
        print("*" *height)#wants to print * as the height
    else:
        print("*", " "*(height -2)+ "*")#prints * subtracted by 2


a=int(input("Enter the mark of maths:"))
b=int(input("Enter the mark of english:"))
c=int(input("Enter the mark of malayalam:"))
d=int(input("Enter the mark of hindi:"))
e=int(input("Enter the mark of science:"))
sum=a+b+c+d+e
avg=sum/5
if(avg>80):
    print("Grade A+")
elif(avg>75):
    print("Grade A")
elif(avg>65):
    print("Grade B+")
elif(avg>55):
    print("Grade B")
elif(avg>45):
    print("Grade C+")
elif(avg>35):
    print("grade C")
else:
    print("Failed")
    

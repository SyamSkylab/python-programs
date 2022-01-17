def trise(a,b,c):
    sum=a+b+c
    print("sum of the numbers is:",sum)
    if(a==b==c):
        return(3*sum)
    else:
        print("numbers are not equal")
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Enter third number:"))
s=trise(x,y,z)
print(s)
      

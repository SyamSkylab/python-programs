n=int(input("Enter the number"))
a=0
b=1
c=a+b
print(" ",a,b)
for i in range(1,n+1,1):
    print(" ",a+b)
    #c=a+b
    a,b=b,a+b
    

     

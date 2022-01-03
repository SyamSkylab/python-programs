n=int(input("Enter the number"))
a=0
b=1
c=a+b
print(" ",a)
for i in range(1,n+1,1):
    print(" ",c)
    c=a+b
    a=b
    b=c

     

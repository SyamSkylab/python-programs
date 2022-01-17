def Sum(n):
    s=0
    r=0
    while(n>0):
        r=n%10
        s=s+r
        n=n//10
    return(s)
x=int(input("Enter the number"))
a=Sum(x)
print("Sum=",a)

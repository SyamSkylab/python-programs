def Neon(x):
    s=0
    n=(x*x)
    while(n>0):
        r=n%10
        s=s+r
        n=n//10
    if(x==s):
        print("NUMBER",x,"IS NEON")
    else:
        print("NUMBER IS NOT NEON")
a=int(input("Enter The Number:"))      
Neon(a)

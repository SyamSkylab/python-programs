def Armstrong(x):
    s=0
    n=x
    while(n>0):
        r=n%10
        s=s+(r*r*r)
        n=n//10
    if(x==s):
        print("NUMBER",x,"IS ARMSTRONG")
    else:
        print("NUMBER IS NOT ARMSTRONG")
a=int(input("Enter The Number:"))      
Armstrong(a)

def Fact(x):
    for i in range(1,x+1,1):
        if(x%i==0):
            print(i)
a=int(input("Enter the number:"))
Fact(a)

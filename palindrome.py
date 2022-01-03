n=int(input("Enter the number"))
rev=0
i=n
while(i>0):
    r=i%10
    rev=(rev*10)+r
    i=i//10
if(rev==n):
    print("The Number is palindrome")
else:
    print("The Number is not palindrome")

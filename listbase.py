L1=list(input("Enter the values of first number:"))
L2=list(input("Enter the values of second number:"))
s1=0
s2=0
if(len(L1)==len(L2)):
    print("Lists are same in length")
else:
    print("List are not same in length")
for i in range(0,len(L1)):
    s1=s1+int(L1[i])

for i in range(0,len(L2)):
    s1=s1+int(L2[i])

if(s1==s2):
    print("sum is same")
else:
    print("sum is not same")
for i in range(0,len(L1)):
    for j in range(0,len(L2)):
        if(L1[i]==L2[j]):
            print(L1[i])
            for k in range(0,len(L2)):
                if(L2[k]==L1[i]):
                    L2[k]="#"
            
        

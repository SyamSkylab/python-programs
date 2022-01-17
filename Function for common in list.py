def comm(L3,L4):
    for i in range(0,len(L3)):
        for j in range(0,len(L4)):
            if(L3[i]==L4[j]):
                if(L3[i]!=" "):
                    return("true")
L1=list(input("Enter fist list"))
L2=list(input("Enter second list"))
c=comm(L1,L2)
if(c=="true"):
    print("TWO LISTS HAVE COMMON ELEMENTS")
else:
    print(c)
    

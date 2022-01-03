for i in range(1,16,1):
    if(i%3==0 and i%5==0):
        print("c",end=" ")
    elif(i%3==0):
        print("A",end=" ")
    elif(i%5==0):
        print("B",end=" ")
    else:
        print(i,end=" ")

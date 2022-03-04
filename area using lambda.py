a=int(input("Enter the lenght of one side of the square:"))
area1=lambda a : a*a
x=area1(a)
print("Area of square",x)
b=int(input("Enter the height of the rectangle:"))
c=int(input("Enter the width of the rectangle:"))
area2=lambda b,c : b*c
x2=area2(b,c)
print("Area Of Rectangle:",x2)
base=int(input("Enter the base of the traingle:"))
h=int(input("Enter the height of the traingle:"))
area3=lambda base,h :(0.5*base*h)
x3=area3(base,h)
print("Area of traingle:",x3)

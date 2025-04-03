import math

print("AX²-BX+C")
a= int(input("Enter A Value Of A"))
b= int(input("Enter A Value Of B"))
c= int(input("Enter A Value Of C"))

s = (b**2)-(4*a*c)

if(s>0):
    r1 = -b + math.sqrt(s)/(2*a)
    r2 = -b - math.sqrt(s)/(2*a)
    print("The Roots Are ",r1,r2)
elif(s==0):
    r1=r2= -b/(2*a)
    print("The Root are ",r1,r2)
else:
    print("roots are imaginary")
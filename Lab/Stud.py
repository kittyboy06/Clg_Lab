def inp():
    n = input("Enter the Name Of Student: ")
    p = int(input("Enter the Physics Mark: "))
    c = int(input("Enter the Chemistry Mark: "))
    m = int(input("Enter the Maths Mark: "))
    return n,p,c,m

no = int(input("Enter the number of Students: "))
name,Maths,Chemistry,Physics,avg = [],[],[],[],[]
for i in range(no):
    n,p,c,m = inp()
    name.append(n)
    Physics.append(p)
    Chemistry.append(c)
    Maths.append(m)
    avg.append((p+c+m)/3)
print("Fails:")
for i in range(no):
    if(avg[i] <= 40):
        print("{} is Fail".format(name[i]))
        
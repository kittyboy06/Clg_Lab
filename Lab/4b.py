import math
n = int(input("Enter a Number: "))
if n < 2:
    print("Invalid Input")
div = 2
_prime = True
while div <= math.sqrt(n):
    if n % div == 0:
        _prime = False
        break
    div += 1
if _prime:
    print("Prime Number")
else:
    print("Not a Prime Number")
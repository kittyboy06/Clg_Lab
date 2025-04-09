def Sq_root(n):
    rem = n/2
    while (rem ** 2 - n > 10 ** -6):
        rem = 0.5 * (rem + n / rem)
    return rem

def cu_root(n):
    rem = n
    while (rem ** 3 - n > 10 ** -6):
        rem = (2 * rem + n / (rem ** 2)) / 3
    return rem

n = int(input("Enter a number: "))
print("Square root and Cube root of {} is {},{}".format(n, Sq_root(n), cu_root(n)))
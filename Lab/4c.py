import math
n = int(input("Enter the number of rows for Pascal's Triangle: "))
pascals_triangle = []
for i in range(n):
    row = []
    for k in range(i + 1):
        value = math.comb(i, k)
        row.append(value)
    print(" ".join(str(num) for num in row))
    pascals_triangle.append(row)

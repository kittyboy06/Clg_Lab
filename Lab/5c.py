col = []
print("Enter the colors(0 to exit):")
while True:
    c = input()
    if c == "0":
        break
    else:
        col.append(c)
n = input("Enter the colors to find in the list:")
for i in col:
    if(n == i):
        print(f"Found in List")
else:
    print("Not found")
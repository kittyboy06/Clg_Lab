words = []
print("Enter the Words(0 to exit)")
while True:
    n = input()
    if n == "0":
        break
    words.append(n)
alpha = input("Enter a letter to search its word:").lower()
print(f"Words Starting with {alpha}")
for index,word in enumerate(words):
    if word.lower().startswith(alpha):
        print(f"Index {index}:{word}")
    else:
        print("Not found")
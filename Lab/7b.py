def str_len(s):
    if s == "":
        return 0
    else:
        return 1 + str_len(s[1:])
str = input("Enter a word:")
print(f"The word contain {str_len(str)} letters")
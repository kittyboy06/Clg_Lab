def palindrome_checker(s):
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return palindrome_checker(s[1:-1])
    else:
        return False

str_input = input("Enter a string: ")
print("Palindrome:" , palindrome_checker(str_input))

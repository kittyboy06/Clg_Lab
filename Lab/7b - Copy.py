def string_length(s):
    if s == "":
        return 0
    return 1 + string_length(s[1:])
string=input("enter a string:")
length=string_length(string)
print("Length of the string:",length)

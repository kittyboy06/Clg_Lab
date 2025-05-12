f1 = 'myFile.txt'

try:
    with open(f1, 'r') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            count += 1
            print(f"Line {count}: {line.strip()}")
        print(f"\nThe file has {count} lines")

except FileNotFoundError:
    print(f"The file {f1} was not found")

except EOFError:
    print("End of file error occurred")

except Exception as e:
    print("An error occurred:", e)

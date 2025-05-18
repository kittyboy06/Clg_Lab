# Function prototype 1
def BMI_Calc1():
    data = []
    for i in range(5):
        height = float(input(f"Enter height (m) for person {i+1}: "))
        weight = float(input(f"Enter weight (kg) for person {i+1}: "))
        data.append((height, weight))
    for height, weight in data:
        bmi1 = weight / (height ** 2)
        print(f"BMI: {bmi1:.2f}")

# Function prototype 2
def BMI_Calc2(data):
    for height, weight in data:
        bmi2 = weight / (height ** 2)
        print(f"BMI: {bmi2:.2f}")
    return len(data)

# Function prototype 3
def BMI_Calc3():
    data = []
    for i in range(5):
        height = float(input(f"Enter height (m) for person {i+1}: "))
        weight = float(input(f"Enter weight (kg) for person {i+1}: "))
        bmi3 = weight / (height ** 2)
        data.append((height, weight, bmi3))
    return data

# Function prototype 4
def BMI_Calc4(height, weight):
    return weight / (height ** 2)

# Main program
print("Choose a function prototype to use (1-4):")
choice = int(input("Enter your choice: "))

if choice == 1:
    BMI_Calc1()

elif choice == 2:
    data = []
    for i in range(5):
        height = float(input(f"Enter height (m) for person {i+1}: "))
        weight = float(input(f"Enter weight (kg) for person {i+1}: "))
        data.append((height, weight))
    length = BMI_Calc2(data)
    print(f"Length of data: {length}")

elif choice == 3:
    data1 = BMI_Calc3()
    for height, weight, bmi in data1:
        print(f"BMI: {bmi:.2f}")

elif choice == 4:
    for i in range(5):
        height = float(input(f"Enter height (m) for person {i+1}: "))
        weight = float(input(f"Enter weight (kg) for person {i+1}: "))
        bmi4 = BMI_Calc4(height, weight)
        print(f"BMI: {bmi4:.2f}")

else:
    print("Invalid choice.")
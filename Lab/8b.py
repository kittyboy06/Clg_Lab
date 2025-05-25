try:
    with open('student_record.txt', 'r') as f:
        lines = f.readlines()

    student_records = []
    for line in lines:
        name, age = line.strip().split()
        student_records.append((name, int(age)))

    sorted_records = sorted(student_records, key = lambda x : x[0])

    print("NAME AGE")
    for record in sorted_records:
        print(f"{record[0]} {record[1]}")

except FileNotFoundError:
    print("File not found")
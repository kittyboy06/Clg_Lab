stud_name = []
n = int(input("Enter number of students: "))
marks,avg,gra = [],[],[]
for i in range(n):
    stud_name.append(input("Enter student name: "))
    marks.append(list(map(int, input("Enter marks in Physics, Maths and Chemistry: ").split())))
    avg.append(sum(marks[i])/3)
    if avg[i] >= 90:
        gra.append("A")
    elif avg[i] >= 80:
        gra.append("B")
    elif avg[i] >= 70:
        gra.append("C")
    elif avg[i] >= 60:
        gra.append("D")
    elif avg[i] >= 50:
        gra.append("E")
    else:
        gra.append("F")
for i in range(n):
    print("Student Name: ", stud_name[i])
    print("Marks: ", marks[i])
    print("Average: ", avg[i])
    print("Grade: ", gra[i])


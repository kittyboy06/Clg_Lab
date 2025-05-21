stud = {"Arshi":[95,99,98],"Afsal":[90,95,97],"Sooriya":[30,32,45]}
updated_stud = {}
for name,marks in stud.items():
    tot = sum(marks)
    avg = tot/len(marks)
    updated_stud[name] = {"Total":tot,"Average":avg}
top = max(updated_stud.items(),key = lambda item:item[1]["Total"])
print("Updated Dictoinary:",updated_stud)
print("Topper:",top)
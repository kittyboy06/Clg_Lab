import datetime
tuple1 = tuple(map(int,input("Enter date month year: ").split()))
tuple2 = tuple(map(int,input("Enter date month year: ").split()))
date1 = datetime.date(tuple1[2], tuple1[1], tuple1[0])
date2 = datetime.date(tuple2[2], tuple2[1], tuple2[0])
diff = date2 - date1
print("The difference between the two dates is:", abs(diff).days, "days")

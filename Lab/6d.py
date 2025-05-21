import random
random_set = set(random.randint(15,45) for i in range(10))
print("Orginal Set:",random_set)
lessthan = 0
mod_Set = set()
for num in random_set:
    if num < 30:
        lessthan+=1
    if num <= 35:
        mod_Set.add(num)
print("Count of numbers less than 30:",lessthan)
print("Modified Set",mod_Set)
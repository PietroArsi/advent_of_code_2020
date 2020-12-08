with open("inputs/day6.txt", "r") as f:
    lines = f.read()
    groups = [l.replace("\n", "") for l in lines.split("\n\n")]
    groups2 = [l.split("\n") for l in lines.split("\n\n")]

count=0

for x in groups:
    answers=set()
    for a in x:
        answers.add(str(a))
    count+=len(answers)

print(f"First count is {count}")

count2=0

for x in groups2:
    answers2=list()
    for line in x:
        new_s=set([c for c in line])
        answers2.append(set(new_s))
    
    final_set=answers2[0]
    for s in answers2[1:]:
        final_set = final_set & s
    
    count2+=len(final_set)

print(f"Second count is {count2}")
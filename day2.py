import re

with open("inputs/day2.txt", "r") as f:
    lines = [l.replace("\n", "") for l in f.readlines()]

correct=0
for line in lines:
    #print(line)
    r = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
    #print(r.groups())
    #print(f"{r.groups()[2]} appeared {len(re.findall(r.groups()[2], r.groups()[3]))} times, should be between {r.groups()[0]} and {r.groups()[1]}")
    if(int(r.groups()[0]) <= len(re.findall(r.groups()[2], r.groups()[3])) <= int(r.groups()[1])):
        correct+=1

print(f"There are {correct} correct passwords by first policy")

correct=0
for line in lines:
    #print(line)
    r = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
    #print(r.groups())
    #print(f"{r.groups()[2]} appeared {len(re.findall(r.groups()[2], r.groups()[3]))} times, should be between {r.groups()[0]} and {r.groups()[1]}")
    pwd=r.groups()[3]
    if((pwd[int(r.groups()[0])-1]==r.groups()[2] and pwd[int(r.groups()[1])-1]!=r.groups()[2]) or (pwd[int(r.groups()[0])-1]!=r.groups()[2] and pwd[int(r.groups()[1])-1]==r.groups()[2])):
        correct+=1

print(f"There are {correct} correct passwords by second policy")


with open("inputs/test1.txt", "r") as f:
    lines=[int(l.replace("\n", "")) for l in f.readlines()]

for a in range(len(lines)):
    for b in range(len(lines[a:])):
        print(f"Checking {a}-{b}")
        if(lines[a]+lines[b]==2020):
            print(f"2020 found! Result 1 is: {lines[a]*lines[b]}")

for a in lines:
    for b in lines:
        for c in lines:
            if(a+b+c==2020):
                print(f"2020 found! Result 2 is: {a*b*c}")
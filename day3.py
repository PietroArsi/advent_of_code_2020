configs=dict()
configs["0"]={"x":1, "y":1}
configs["1"]={"x":3, "y":1}
configs["2"]={"x":5, "y":1}
configs["3"]={"x":7, "y":1}
configs["4"]={"x":1, "y":2}

with open("inputs/day3.txt", "r") as f:
    lines = [l.replace("\n", "") for l in f.readlines()]
    lines = [list(l) for l in lines]

MAXLENX=len(lines[0])-1
MAXLENY=len(lines)-1

for c in configs:
    trees=0
    counter=0
    x=0
    y=0
    forest=[[l2 for l2 in l1] for l1 in lines]
    while(True):
        #new position
        newX=x+configs[c]["x"]
        newY=y+configs[c]["y"]
        #print(lines[newY][newX])
        #print(f"{newY} - {newX}")
        if(newY>MAXLENY):
            break
        if(newX>MAXLENX):
            newX=newX-MAXLENX-1
        if(forest[newY][newX]=="#"):
            forest[newY][newX]="X"
            trees+=1
        else:
            forest[newY][newX]="O"
        x=newX
        y=newY
        counter+=1
    
    with open(f"day3processed{c}.txt", "w") as f:
        for x in forest:
            for y in x:
                f.write(y)
            f.write("\n")
    
    configs[c]["trees"]=trees

result=1
for c in configs:
    result*=configs[c]["trees"]

print(f"Result is {result} trees")

# with open("day3processed.txt", "w") as f:
#     for x in lines:
#         for y in x:
#             f.write(y)
#         f.write("\n")


import re
import time

with open("inputs/day7.txt", "r") as f:
    lines = [l.replace("\n", "") for l in f.readlines()]

bags=dict()
for x in lines:
    bagname = re.match(r"^(\D+) bags contain", x).group(1)
    #print(bagname)
    contained = re.findall(r"(?: (\d) (\D+) bag(?:s)?(?:\.|,))", x)
    #print(contained)

    contained_dict=dict()
    for bag in contained:
        contained_dict[str(bag[1])] = int(bag[0])

    bags[str(bagname)]=contained_dict

#processed_bags=dict(bags)
count1=0  
for bag in bags:
    if(bag!="shiny gold"):
        #print(f"Reading {bag} bag")
        lifo=list()
        first=True
        lifo.append(bag)
        nextbag=False
        while(not nextbag):
            try:
                poppedbag = lifo.pop()
                #print(f"Found {poppedbag} bag")
                for x in bags[str(poppedbag)]:
                    if(str(x)=="shiny gold"):
                        #print(f"{poppedbag} can contain shiny gold bag!")
                        count1+=1
                        nextbag=True
                        break
                    else:
                        lifo.append(str(x))
            except IndexError:
                break
            first=False
        #print("")

print(f"{count1} bags can contain a shiny gold bag")

#V2
inizio=time.time()

lifo=list()
lifo.append(list(["shiny gold", 1]))

processed_bags=list()
other_bags=0

for bag in lifo:
    #print(bag)
    for x in bags[bag[0]]:
        #print(bags[bag[0]][str(x)])
        mult=int(bags[bag[0]][str(x)])
        processed_bags.append(list([str(x), mult*int(bag[1])]))
    
    #print(processed_bags)

    for x in processed_bags:
        if(len(bags[str(x[0])])>0):
            other_bags+=int(x[1])
            lifo.append(x)
            processed_bags.remove(x)

count2=0
for x in processed_bags:
    count2+=x[1]

fine=time.time()

print(f"Shiny gold bag can contain {count2+other_bags} bags")
print(f"\nElapsed: {fine-inizio} s")








# inizio=time.time()

# lifo=list()
# lifo.append("shiny gold")

# single_bags=list()
# other_bags=0

# for bag in lifo:
#     #print(bag)
#     for x in bags[bag]:
#         mult=int(bags[bag][x])
#         for times in range(mult):
#             single_bags.append(str(x))

#     # single_bags_len=len(single_bags)
    
#     for x in single_bags:
#         if(len(bags[x])>0):
#             other_bags+=1
#             lifo.append(x)
#             single_bags.remove(x)

# fine=time.time()

# print(f"Shiny gold bag can contain {len(single_bags)+other_bags} bags")
# print(f"Elapsed: {fine-inizio} s")

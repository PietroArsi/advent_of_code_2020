import re

parameters={"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}

with open("inputs/day4.txt", "r") as f:
    info=""
    for x in f.readlines():
        info+=x
        
info=[l.replace("\n", " ") for l in info.split("\n\n")]

database=dict()
for person in range(len(info)):
    for p in parameters:
        if(person not in database):
            database[person]=dict()
            
        r = re.compile(fr".*{p}:(\S+).*")
        x = r.match(info[person])
        # if(len(x.groups())>1):
        #     break
        if(x==None):
            database[person][p]=None
        else:
            database[person][p]=r.match(info[person]).groups()[0]

valid_ids=0
for x in database:
    valid=True
    for p in parameters:
        if(p!="cid" and database[x][p]==None):
            valid=False
            break
    if(valid):
        valid_ids+=1

print(f"There are {valid_ids} valid ids")

colors = list(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

#print(database)

valid_ids=0
for x in database:
    valid=True
    for p in parameters:
        if(p!="cid" and database[x][p]==None):
            valid=False
            break
    if(valid):
        if(1920 <= int(database[x]["byr"]) <= 2002):
            if(2010 <= int(database[x]["iyr"]) <= 2020):
                if(2020 <= int(database[x]["eyr"]) <= 2030):
                    if(re.match(r"\d+(cm|in)", database[x]["hgt"])):
                        a=re.match(r"(\d+)cm", database[x]["hgt"])
                        b=re.match(r"(\d+)in", database[x]["hgt"])
                        if(a and 150 <= int(a.groups()[0]) <= 193) or (b and 59 <= int(b.groups()[0]) <= 76):
                            if(re.match(r"^#([0-9]|[a-f]){6}$", database[x]["hcl"])):
                                if(database[x]["ecl"] in colors):
                                    if(re.match(r"^([0-9]){9}$", database[x]["pid"])):
                                        valid_ids+=1
        #                             else:
        #                                 print("pid invalid")
        #                         else:
        #                             print("ecl invalid")
        #                     else:
        #                         print("hcl invalid")
        #                 else:
        #                     print("cm/in measure invalid")
        #             else:
        #                 print("no cm or in substring found")
        #         else:
        #             print("eyr invalid")                        
        #     else:
        #         print("iyr invalid")
        # else:
        #     print("byr invalid")

print(f"There are {valid_ids} correct ids")
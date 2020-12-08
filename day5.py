import sys

with open("inputs/day5.txt", "r") as f:
    passports=[l.replace("\n", "") for l in f.readlines()]

seat_IDs=list()
seats=list()

for p in passports:
    rows_a=0
    rows_b=127
    columns_a=0
    columns_b=7

    for x in range(7):
        if(p[x]=="F"):
            rows_b -= (rows_b - rows_a+1)/2
        elif(p[x]=="B"):
            rows_a += (rows_b - rows_a+1)/2
        #print(f"{rows_a} - {rows_b}")

    if(rows_a!=rows_b):
        print("There was an error with binary search")
        sys.exit()
    
    for x in range(7, 10):
        if(p[x]=="L"):
            columns_b -= (columns_b - columns_a+1)/2
        elif(p[x]=="R"):
            columns_a += (columns_b - columns_a+1)/2
        #print(f"{columns_a} - {columns_b}")
    
    if(columns_a!=columns_b):
        print("There was an error with binary search")
        sys.exit()
    
    seats.append(list([int(columns_b), int(rows_b)]))
    seat_IDs.append(int(rows_b * 8 + columns_b))

seat_IDs.sort()

print(f"Highest ID is {max(seat_IDs)}")

for x in range(min(seat_IDs), max(seat_IDs)+1):
    if(x not in seat_IDs and x-1 in seat_IDs and x+1 in seat_IDs):
        print(f"Missing ID is {x}")
        break

#print([x for x in range(min(seat_IDs), max(seat_IDs)+1) if(x not in seat_IDs and x-1 in seat_IDs and x+1 in seat_IDs)][0])
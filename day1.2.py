import random
import time

with open("inputs/day1.txt", "r") as f:
    lines=[int(l.replace("\n", "")) for l in f.readlines()]

partenza = time.time()

while(True):
    a=random.choice(lines)
    b=random.choice(lines)
    if(a+b==2020):
        print(f"Result is: {a*b}")
        break

arrivo = time.time()

print(f"Time used for task 1: {arrivo-partenza} seconds")

partenza = time.time()

while(True):
    a=random.choice(lines)
    b=random.choice(lines)
    c=random.choice(lines)
    if(a+b+c==2020):
        print(f"Result is: {a*b*c}")
        break

arrivo = time.time()

print(f"Time used for task 2: {arrivo-partenza} seconds")
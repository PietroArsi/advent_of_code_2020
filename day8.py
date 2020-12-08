with open("inputs/day8.txt", "r") as f:
    lines=f.readlines()

instructions = [list([str(l.replace("\n", "").split(" ")[0]), int(l.replace("\n", "").split(" ")[1])]) for l in lines]

cached_instructions=set()
accumulator=0
ip=0


while(True):
    instruction=instructions[ip][0]
    amount=instructions[ip][1]
    #print(f"[{ip}]: {instruction} {amount}")
    if(int(ip) not in cached_instructions):
        cached_instructions.add(int(ip))
    else:
        print(f"Accumulator value is {accumulator}")
        break
    if(instruction=="nop"):
        ip+=1
    elif(instruction=="acc"):
        accumulator+=amount
        ip+=1
    elif(instruction=="jmp"):
        ip+=amount

for mod in range(len(instructions)):
    #print(mod)
    if(instructions[mod][0]!="jmp" and instructions[mod][0]!="nop"):
        continue
    modified_instructions=[list([str(i[0]), int(i[1])]) for i in instructions]
    if(modified_instructions[mod][0]=="jmp"):
        modified_instructions[mod][0]="nop"
    else:
        modified_instructions[mod][0]="jmp"
    cached_instructions=set()
    accumulator=0
    ip=0

    loop=False
    while(True):
        instruction=modified_instructions[ip][0]
        amount=modified_instructions[ip][1]
        #print(f"[{ip}]: {instruction} {amount}")
        if(int(ip) not in cached_instructions):
            cached_instructions.add(int(ip))
        else:
            #print("loop!")
            loop=True
            break
        if(instruction=="nop"):
            ip+=1
        elif(instruction=="acc"):
            accumulator+=amount
            ip+=1
        elif(instruction=="jmp"):
            ip+=amount
        if(ip>=len(modified_instructions)):
            break

    if(not loop):
        print(f"Fixed boot loop: accumulator value is {accumulator}")
        break
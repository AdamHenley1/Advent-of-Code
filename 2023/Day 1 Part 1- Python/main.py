#56049
o = []
to = []
input_file = open("/Users/adamhenley/Documents/GitHub/Advent-of-Code/2023/Day 1 Part 1- Python/inputs.txt", 'r')  

for i in input_file.readlines():
    o.append(i)
for z in range(len(o)):
    t = 0
    v = 0
    f = 0 
    l = 0
    le = o[z]
    for e in range(len(le)):
        if le[e].isdigit() == True:
            if t == 0:
                f = le[e]
                t += 1
                v += 1
            else: 
                l = le[e]
                v += 1 
    if v == 1:
        ts = str(f)+ str(f)
        to.append(ts)
    else:
        ts = str(f)+str(l)
        to.append(ts)
c = 0
for i in range(len(to)):
    to[i] = int(to[i])
for i in range(len(to)):
    c += to[i]
print(c)
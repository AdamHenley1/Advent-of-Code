import os
o = []
total = []
input_file = open("/Users/adamhenley/Documents/GitHub/Advent-of-Code/2023/Day 1 Part 2- Python/inputs.txt", 'r')  
for i in input_file.readlines():
    o.append(i)


for z in range(len(o)):
    t = 0
    f = 0 
    p = 0
    l = o[z]
    l = l.replace("one","o1e")
    l = l.replace("two","t2o")
    l = l.replace("three","t3e")
    l = l.replace("four","f4r")
    l = l.replace("five","f5e")
    l = l.replace("six","s6x")
    l = l.replace("seven","s7n")
    l = l.replace("eight","e8t")
    l = l.replace("nine","n9e")
    for e in range(len(l)):
        if l[e] == '1' or l[e] == '2' or l[e] == '3'or l[e] == '4'or l[e] == '5'or l[e] == '6'or l[e] == '7'or l[e] == '8'or l[e] == '9':
            if t == 0:
                f = l[e]
                t += 1
            elif t >= 1: p=l[e]
    if p == 0:
        p = f
    totals = str(f)+str(p)
    total.append(totals)
complete = 0
for i in range(len(total)):
    complete += int(total[i])
print(complete)
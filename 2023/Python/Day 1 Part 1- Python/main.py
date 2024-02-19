#56049
c=0
h=open("/Users/adamhenley/Documents/GitHub/Advent-of-Code/2023/Day 1 Part 1- Python/inputs.txt",'r')  
for z in h.readlines():
    t=0
    l=0
    p=z
    for e in p:
        if e.isdigit()==True:
            if t==0:
                f=e
                t+=1
            elif t>=1:l=e
    if l==0:l=f
    g=str(f)+str(l)
    c+=int(g)
print(c)
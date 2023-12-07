o = []
split = []
total = []
red = 12
green = 13
blue = 14
input_file = open("/Users/adamhenley/Documents/python_advent_of_code/2/input.txt", 'r')  
for i in input_file.readlines():
    o.append(i)
c = 0
for i in range(100):
    x = o[i]
    for z in range(len(o[i])):
        if x[z].isdigit() == True and x[z+1].isdigit() == False:
            if x[z].isdigit() == True and x[z+2:z+5] == "red" and int(x[z]) < 12:
                c += 1
            elif x[z].isdigit() == True and x[z+2:z+6] == "green" and int(x[z]) < 13:
                c += 1
            if x[z].isdigit() == True and x[z+2:z+6] == "blue" and int(x[z]) < 14:
                c += 1
    print(x[5])
    if c == 9:
        total.append(x[5])
    c = 0
    print(total)
#only 12 red cubes, 13 green cubes, and 14 blue cubes
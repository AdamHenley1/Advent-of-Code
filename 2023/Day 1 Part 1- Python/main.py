import os
ones = []
total = []
input_file = open("/Users/adamhenley/Documents/python_advent_of_code/1/inputs.txt", 'r')  
ranges = ["1","2","3","4","5","6","7","8","9","0"]
for i in input_file.readlines():
    ones.append(i)
for z in range(len(ones)):
    temp = 0
    var = 0
    first = 0 
    last = 0
    letter = ones[z]
    for e in range(len(letter)):
        #print(letter[e])
        if letter[e] == '1' or letter[e] == '2' or letter[e] == '3'or letter[e] == '4'or letter[e] == '5'or letter[e] == '6'or letter[e] == '7'or letter[e] == '8'or letter[e] == '9'or letter[e] == '10':
            if temp == 0:
                first = letter[e]
                temp += 1
                var += 1
                #print("first",first)
            elif temp >= 1: 
                last = letter[e]
                var += 1 
                #print("last",last)
            #print(first,last)
        else: pass
    if var == 1:
        totals = str(first)+ str(first)
        total.append(totals)
    else:
        totals = str(first)+str(last)
        total.append(totals)
complete = 0
for i in range(len(total)):
    total[i] = int(total[i])
for i in range(len(total)):
    complete += total[i]
print(complete)
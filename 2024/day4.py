#day4
import sys
sys.path.insert(0, 'C:/Users/iker_/Documents/AdventOfCode')
from AoC import * 

# part 1
ans = 0
file = "2024/inputs/day4.txt"
with open(file) as f:
    lines = f.readlines()
    lines = [i.replace("\n","") for i in lines]
for j in range(len(lines)):
    line = lines[j]
    res = [i for i in range(len(line)) if line[i]=="X"] 
    for idx in res:
        for x in [0,1,-1]:
            for y in [0, 1,-1]:
                if idx+3*y<0 or j+3*x <0:
                    continue
                try:
                    word = lines[j][idx]+lines[j+1*x][idx+1*y]+lines[j+2*x][idx+2*y]+lines[j+3*x][idx+3*y]
                    if word == "XMAS" : ans+=1
                except IndexError:
                    pass
print(ans)

# part 2
ans = 0
with open(file) as f:
    lines = f.readlines()
    lines = [i.replace("\n","") for i in lines]
for j in range(len(lines)):
    line = lines[j]
    res = [i for i in range(len(line)) if line[i]=="A"] 
    for idx in res:
        if j-1<0 or idx-1<0:
            continue
        try:
            dig1 = lines[j-1][idx-1]+"A"+lines[j+1][idx+1]
            dig2 = lines[j-1][idx+1]+"A"+lines[j+1][idx-1]
        except IndexError:
            continue
        if (dig1=="SAM" or dig1=="MAS") and (dig2=="SAM" or dig2=="MAS"):
            ans +=1
print(ans)

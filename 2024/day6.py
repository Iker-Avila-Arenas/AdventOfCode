#day6
import sys
sys.path.insert(0, 'C:/Users/iker_/Documents/AdventOfCode')
from AoC import * 

def find_blocks(lines):
    blocks = []
    y = 0
    for line in lines:
        l = list(line)
        for x in range(len(l)):
            if l[x] == "#":
                blocks.append([y,x])
        y+=1
    return blocks

def find_start(lines):
    blocks = []
    y = 0
    for line in lines:
        l = list(line)
        for x in range(len(l)):
            if l[x]==">" or l[x]=="<" or l[x]=="^" or l[x]=="v":
                return y, x, l[x]
        y+=1
    return None

def find_path(start_y, start_x, start_dir, blocks, bounds):
    path = []
    loop = True
    dir = start_dir
    x = start_x
    y = start_y
    path.append([y,x,dir])
    while loop:
        if dir == "^" and [y-1, x] in blocks:
            dir = ">"
        elif dir == ">" and [y, x+1] in blocks:
            dir = "v"
        elif dir == "v" and [y+1, x] in blocks:
            dir = "<"
        elif dir == "<" and [y, x-1] in blocks:
            dir = "^"
        elif dir == "^":
            y = y-1
        elif dir == ">":
            x = x+1
        elif dir == "v":
            y = y+1
        elif dir == "<":
            x = x-1
        if [y,x,dir] in path:
            return path, True
        elif x==0 or y==0 or x==bounds[1]-1 or y==bounds[0]-1:
            path.append([y,x,dir])
            return path, False
        else:
            path.append([y,x,dir])
    
#part 1
file = "2024/inputs/day6.txt"
with open(file) as f:
    lines = f.read().splitlines()
bounds = len(lines), len(lines[0])
blocks = find_blocks(lines)
y, x, dir = find_start(lines)
path = find_path(y,x,dir,blocks,bounds)

uniques = []
for p in path[0]:
    new = [p[0],p[1]]
    if new not in uniques:
        uniques.append(new)
print(len(uniques))

#part2
ans = 0
iter = 0
test = []
y_s, x_s, dir_s = find_start(lines)
path = find_path(y,x,dir,blocks,bounds)
for p in path[0][1:]:
    pos = [p[0],p[1]]
    if pos not in test:
        test.append(pos)

for p in test:
    iter+=1
    print(iter/len(path[0])*100, end="\r")
    cond = False
    y = p[0]
    x = p[1]
    _, cond = find_path(y_s,x_s,dir_s,blocks+[[y,x]],bounds)
    # if dir=="^" and "#" in list(lines[y][x:]):
    #     _, cond = find_path(y,x,dir,blocks+[[y-1,x]],bounds)
    # elif dir==">" and "#" in [lines[j][x] for j in range(y+1,bounds[0])]:
    #     _, cond = find_path(y,x,dir,blocks+[[y,x+1]],bounds)
    # elif dir=="v" and "#" in list(lines[y][0:x]):
    #     _, cond = find_path(y,x,dir,blocks+[[y+1,x]],bounds)
    # elif dir=="<" and "#" in [lines[j][x] for j in range(0,y+1)]:
    #     _, cond = find_path(y,x,dir,blocks+[[y,x-1]],bounds)
    if cond:
        ans+=1
print()
print(ans)
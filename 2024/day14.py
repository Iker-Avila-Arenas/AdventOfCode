# day 14

import os
clear = lambda: os.system('cls')

def draw_robots(pos, bounds):
    grid = [" "*int(bounds.real)]*int(bounds.imag)
    clear()
    for p in pos:
        if p.real!=0:
            grid[int(p.imag)-1] = grid[int(p.imag)-1][:int(p.real)-1] + "0" + grid[int(p.imag)-1][int(p.real):]
        else:
            grid[int(p.imag)-1] = grid[int(p.imag)-1][:int(p.real)-1] + "0"
    for g in grid:
        print(g)

file = "inputs/day14.txt"
with open(file) as f:
    lines = f.read().splitlines()
bounds = 101+103*1j
cuadrant_count = [0,0,0,0]
positions = []
vels = []
for line in lines:
    values = line[2:].replace(" v=",",").split(",")
    p = int(values[0])+int(values[1])*1j
    positions.append(p)
    v = int(values[2])+int(values[3])*1j
    vels.append(v)
    p_fin = p+v*100
    p_cycle = p_fin.real%bounds.real+p_fin.imag%bounds.imag*1j
    if p_cycle.real<bounds.real//2 and p_cycle.imag<bounds.imag//2:
        cuadrant_count[0] += 1
    elif p_cycle.real>bounds.real//2 and p_cycle.imag<bounds.imag//2:
        cuadrant_count[1] += 1
    elif p_cycle.real<bounds.real//2 and p_cycle.imag>bounds.imag//2:
        cuadrant_count[2] += 1
    elif p_cycle.real>bounds.real//2 and p_cycle.imag>bounds.imag//2:
        cuadrant_count[3] += 1
print(cuadrant_count[0]*cuadrant_count[1]*cuadrant_count[2]*cuadrant_count[3])

#part 2
iter=0
inp = ""
while inp=="":
    inp = input()
    for j in range(len(positions)):
        p = positions[j]
        v = vels[j]
        p_fin = p+v
        p_cycle = p_fin.real%bounds.real+p_fin.imag%bounds.imag*1j
        positions[j] = p_cycle
    iter+=1
    draw_robots(positions, bounds)
    print(iter)

# horizontal good: starts at 72, loop is 103
# vertical good: starts at 93, loop is 101
# we need to find the iteration so that: iter=72+103*n=93+101*m
l1 = [72+103*m for m in range(100)]
l2 = [93+101*m for m in range(100)]
m = min(list(set(l1) & set(l2)))

j=0
for line in lines:
    values = line[2:].replace(" v=",",").split(",")
    p = int(values[0])+int(values[1])*1j
    v = int(values[2])+int(values[3])*1j
    p_fin = p+v*m
    p_cycle = p_fin.real%bounds.real+p_fin.imag%bounds.imag*1j
    positions[j] = p_cycle
    j+=1
draw_robots(positions, bounds)

print(m)
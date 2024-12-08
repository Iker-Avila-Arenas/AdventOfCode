#day8
import sys
sys.path.insert(0, 'C:/Users/iker_/Documents/AdventOfCode')
from AoC import * 

grid, bounds = get_grid("2024/inputs/day8.txt")
antenas = set(i for i in "".join(grid))
antenas.remove(".")

res1 = set()
res2 = set()
for a in antenas:
    idx = find_in_grid(grid,a)
    for i1 in idx:
        for i2 in idx:
            vec = 0+0j
            if i1!=i2 and 0<(vec:=2*i1-i2).real<=bounds.real and 0<vec.imag<=bounds.imag : res1.add(vec)
            temp = i1  
            if (vec:=i1-i2) != 0j:
                while 0<temp.real<=bounds.real and 0<temp.imag<=bounds.imag:
                    res2.add(temp)
                    temp+=vec
print(len(res1))
print(len(res2))
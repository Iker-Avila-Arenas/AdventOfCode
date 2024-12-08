#day 5
import sys
sys.path.insert(0, 'C:/Users/iker_/Documents/AdventOfCode')
from AoC import * 

# part 1
ans = 0
file = "2024/inputs/day5.txt"
with open(file) as f:
    lines = f.read().splitlines() 
    d = dict()
    for line in lines:
        if "|" in line:
            list1 = line.split("|")
            n1 = int(list1[0])
            n2 = int(list1[1])
            if n1 in d:
                d[int(list1[0])] += [int(list1[1])]
            else:
                d[int(list1[0])] = [int(list1[1])]
        elif "," in line:
            list1 = line.split(",")
            list1 = [int(i) for i in list1]
            b = True
            for i in reversed(range(len(list1))):
                numbers = d[list1[i]]
                for n in numbers:
                    if n in list1[0:i]:
                        b = False
            if b:
                r = list1[len(list1)//2]
                ans +=r
print(ans)     

# part 2
import random

def func(list1):
    b = True
    for i in reversed(range(len(list1))):
        numbers = d[list1[i]]
        for n in numbers:
            if n in list1[0:i]:
                b = False
                return b, i, n
    return b, None, None


ans = 0
with open(file) as f:
    lines = f.read().splitlines() 
    d = dict()
    for line in lines:
        if "|" in line:
            list1 = line.split("|")
            n1 = int(list1[0])
            n2 = int(list1[1])
            if n1 in d:
                d[int(list1[0])] += [int(list1[1])]
            else:
                d[int(list1[0])] = [int(list1[1])]
        elif "," in line:
            list1 = line.split(",")
            list1 = [int(i) for i in list1]
            b, _, _ = func(list1)
            if not b:
                copy_list1 = list1
                i = 0
                c = False
                while not c:
                    c, key_idx, value = func(copy_list1)
                    value_idx = copy_list1.index(value)
                    copy_list1[key_idx], copy_list1[value_idx] = copy_list1[value_idx], copy_list1[key_idx]
                    c, key_idx, value = func(copy_list1)


                    
                ans += copy_list1[len(copy_list1)//2]
                    
print(ans)

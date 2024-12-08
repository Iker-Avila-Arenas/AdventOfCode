#day 3 
import sys
sys.path.insert(0, 'C:/Users/iker_/Documents/AdventOfCode')
from AoC import * 

import re

#part 1
ans = 0
file = "2024/inputs/day3.txt"
with open(file) as f:
    for t in f.readlines():
        text = str(t)
        pattern = r"mul\(\d+,\d+\)"
        x = re.findall(pattern, text)
        for i in x:
            numbers = re.findall(r"\d+",i)
            n1 = int(numbers[0])
            n2 = int(numbers[1])
            ans += n1*n2
print(ans)

#part 2 - copy from 1
ans = 0
do = 1
with open(file) as f:
    for t in f.readlines():
        text = str(t)
        p1 = r"mul\(\d+,\d+\)"
        p2 = r"do\(\)"
        p3 = r"don\'t\(\)"
        pattern = r"("+p1+"|"+p2+"|"+p3+")"
        x = re.findall(pattern, text)
        for i in x:
            if i=="do()":
                do = 1
                continue
            elif i=="don't()":
                do=0
                continue
            numbers = re.findall(r"\d+",i)
            n1 = int(numbers[0])
            n2 = int(numbers[1])
            ans += n1*n2*do
print(ans)

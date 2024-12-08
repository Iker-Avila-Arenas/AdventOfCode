#day2
import sys
sys.path.insert(0, 'C:/Users/iker_/Documents/AdventOfCode')
from AoC import * 

# part 1
file = "2024/inputs/day2.txt"
ans = 0
with open(file) as f:
    for line in f.readlines():
        array = [int(i) for i in line[0:-1].split(" ")]
        differences = [array[i+1]-array[i] for i in range(len(array)-1)]
        zeros = [i==0 for i in differences]
        if any(zeros):
            continue
        signs = [i/abs(i) for i in differences]
        positives = [i==1.0 for i in signs]
        negatives = [i==-1.0 for i in signs]
        if any(positives) and any(negatives):
            continue
        step_bad = [abs(i)>3 for i in differences]
        if any(step_bad):
            continue
        ans +=1
print(ans)
# part 2
ans = 0
def correct(array):
    differences = [array[i+1]-array[i] for i in range(len(array)-1)]
    zeros = [i==0 for i in differences]
    if any(zeros):
        return 0
    signs = [i/abs(i) for i in differences]
    positives = [i==1.0 for i in signs]
    negatives = [i==-1.0 for i in signs]
    if any(positives) and any(negatives):
        return 0
    step_bad = [abs(i)>3 for i in differences]
    if any(step_bad):
        return 0
    return 1
with open(file) as f:
    for line in f.readlines():
        array = [int(i) for i in line[0:-1].split(" ")]
        n = len(array)
        a = correct(array)
        if a != 1:
            for i in range(n):
                copy = [i for i in array]
                del copy[i]
                a = correct(copy)
                if a==1:
                    break
        ans +=a
print(ans)
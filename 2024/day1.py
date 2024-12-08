#day1
import sys
sys.path.insert(0, 'C:/Users/iker_/Documents/AdventOfCode')
from AoC import * 

import numpy as np
import pandas as pd

data = pd.read_csv("2024/inputs/day1.txt", sep="  ", header=None, engine="python")
list1 = np.sort(np.array(data[0]))
list2 = np.sort(np.array(data[1]))

print(np.sum(np.abs(list1 - list2)))

# day 1, part 2
score = 0
list2 = list2.tolist()
for number in list1:
    score += number*list2.count(number)
print(score)
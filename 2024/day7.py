#day7
import sys
sys.path.insert(0, 'C:/Users/iker_/Documents/AdventOfCode')
from AoC import * 

file = "2024/inputs/day7.txt"
ans = 0
with open(file) as f:
    for line in f.read().splitlines():
        result, operators = line.split(": ")
        result = int(result)
        numbers = operators.split(" ")
        temp = int(numbers[0])
        for i in range(2**(len(numbers)-1)):
            b = bin(i)[2:].zfill(len(numbers)-1)
            for j in range(1,len(numbers)):
                temp = temp + int(numbers[j]) if b[j-1] == "1" else temp * int(numbers[j])
            if temp==result:
                ans+=temp
                break
            else:
                temp=int(numbers[0])
print(ans)

#part 2

ans = 0
with open(file) as f:
    for line in f.read().splitlines():
        result, operators = line.split(": ")
        result = int(result)
        numbers = operators.split(" ")
        temp = int(numbers[0])
        for i in range(3**(len(numbers)-1)):
            b = tobase(i,3).zfill(len(numbers)-1)
            for j in range(1,len(numbers)):
                if b[j-1] == "1" : temp = temp + int(numbers[j])
                elif b[j-1] == "0" : temp = temp * int(numbers[j])
                elif b[j-1] == "2" : temp = int(str(temp)+numbers[j])
                if temp>result:
                    break
            if temp==result:
                ans+=temp
                break
            else:
                temp=int(numbers[0])
print(ans)
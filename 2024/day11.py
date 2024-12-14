#day10

def blink(stones):
    l = stones.split(" ")
    new_stones = ""
    for s in l:
        if s=="0":
            new_stones+="1 "
        elif len(s)%2==0:
            i1 = int(s[:len(s)//2])
            i2 = int(s[len(s)//2:])
            new_stones+=str(i1)+" "+str(i2)+" "
        else:
            i = int(s)
            new_stones+=str(i*2024)+" "
    return new_stones[:-1]

def blink_n(stone,n):
    global dict_stones
    if stone in dict_stones:
        return dict_stones[stone]
    else:
        s = stone
        for i in range(n):
            stone = blink(stone)
        dict_stones[s] = stone
        return stone
    

file = "2024/inputs/day11.txt"
with open(file) as f:
    stones = f.read().splitlines()[0]

for i in range(25):
    stones=blink(stones)
print(len(stones.split(" ")))

#part2

#day 8

def get_grid(filename):
    with open(filename) as f:
        grid = f.read().splitlines()
        bounds = len(grid[0]) + len(grid) * 1j
        return grid, bounds
    
def transpose_grid(grid):
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

def find_in_grid(grid, c):
    return [
        x +y*1j
        for y, line in enumerate(grid)
        for x, char in enumerate(line)
        if char == c
    ]

def find_steps(pos, grid, bounds):
    value = grid[y:=int(pos.imag)][x:=int(pos.real)]
    valid_steps = []
    if x < bounds.real-1 and grid[y][x+1] == value+1:
        valid_steps.append(pos+1)
    if x>=1 and grid[y][x-1] == value+1:
        valid_steps.append(pos-1)
    if y<bounds.imag-1 and grid[y+1][x] == value+1:
        valid_steps.append(pos+1j)
    if y>=1 and grid[y-1][x] == value+1:
        valid_steps.append(pos-1j)
    return valid_steps

def find_trail(trail, grid, bounds):
    global dict_trails
    global all_trails
    pos = trail[-1]
    value = grid[int(pos.imag)][int(pos.real)]
    if value<9:
        next_steps = find_steps(pos,grid,bounds)
        for p in next_steps:
            find_trail(trail+[p], grid, bounds)
    elif value==9:
        all_trails.append(trail)
        if trail[0] in dict_trails:
            dict_trails[trail[0]].add((trail[-1].real, trail[-1].imag))
        else:
            dict_trails[trail[0]]=set()
            dict_trails[trail[0]].add((trail[-1].real, trail[-1].imag))
        


grid, bounds = get_grid("2024/inputs/day10.txt")
idx_zeros = find_in_grid(grid, "0")
grid = [[int(i) for i in line] for line in grid]
ans = 0
ans2 = 0
for zero in idx_zeros:
    dict_trails = dict()
    all_trails = []
    t = find_trail([zero],grid,bounds)
    ans+=len(list(dict_trails.values())[0])
    ans2+=len(all_trails)
print(ans)
print(ans2)
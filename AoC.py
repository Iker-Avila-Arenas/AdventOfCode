#useful functions found on the way

def get_grid(filename):
    with open(filename) as f:
        grid = f.read().splitlines()
        bounds = len(grid[0]) + len(grid) * 1j
        return grid, bounds
    
def transpose_grid(grid):
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

def find_in_grid(grid, c):
    return [
        x+1 +(y+1)*1j
        for y, line in enumerate(grid)
        for x, char in enumerate(line)
        if char == c
    ]


def tobase(n,M):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, M)
        nums.append(str(r))
    return ''.join(reversed(nums))

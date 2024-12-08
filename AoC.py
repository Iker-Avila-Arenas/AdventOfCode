def get_grid(filename):
    with open(filename) as f:
        grid = f.read().splitlines()
        bounds = len(grid[0]) + len(grid) * 1j
        return grid, bounds
    
def transpose_grid(grid):
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

def find_in_grid(grid, c):
    idx = []
    y = 1
    for line in grid:
        l = list(line)
        for x in range(len(l)):
            if l[x] == c:
                idx.append(x + 1 + y * 1j)
        y += 1
    return idx

def tobase(n,M):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, M)
        nums.append(str(r))
    return ''.join(reversed(nums))

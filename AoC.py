def get_grid(filename):
    with open(filename) as f:
        grid = f.read().splitlines()
        bounds = len(grid[0]) + len(grid) * 1j
        return grid, bounds

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

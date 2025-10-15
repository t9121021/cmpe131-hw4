def cacti_number(plot):
    if not isinstance(plot, list) or not plot or not all(isinstance(row, list) for row in plot):
        raise TypeError
    m = len(plot)
    n = len(plot[0])
    if any(len(row) != n for row in plot):
        raise ValueError
    for row in plot:
        for v in row:
            if not isinstance(v, int) or v not in (0, 1):
                raise ValueError
    grid = [row[:] for row in plot]
    def has_adjacent_one(i, j):
        if i > 0 and grid[i-1][j] == 1:
            return True
        if i+1 < m and grid[i+1][j] == 1:
            return True
        if j > 0 and grid[i][j-1] == 1:
            return True
        if j+1 < n and grid[i][j+1] == 1:
            return True
        return False
    added = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and not has_adjacent_one(i, j):
                grid[i][j] = 1
                added += 1
    return added

def runcheck(a, b, visited):
    list1 = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        try:
            if final[a + dx][b + dy].isdigit() and (a + dx, b + dy) not in visited:
                visited, pro = parsenum(a + dx, b + dy, visited)
                list1.append(pro)
        except IndexError:
            pass

    return visited, list1

def parsenum(row, col, visited):
    stage_row = final[row]
    stage = []
    flag = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    if (row, col) in visited:
        return visited, []

    stage.append(stage_row[col])
    visited.add((row, col))

    for dx, dy in directions:
        x, y = row, col
        while 0 <= x + dx < final.shape[0] and 0 <= y + dy < final.shape[1] and final[x + dx][y + dy].isdigit():
            x += dx
            y += dy
            stage.append(final[x][y])
            visited.add((x, y))

    return visited, ''.join(stage)

nummies = []
visited = set()

for a in range(final.shape[0]):
    for b in range(final.shape[1]):
        if not final[a][b].isdigit() and final[a][b] != '.':
            visited, fin = runcheck(a, b, visited)
            nummies.append(fin)

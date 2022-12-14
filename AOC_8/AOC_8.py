map = [x.strip() for x in open("input.txt").readlines()]

def PT(curr, results, x0, x1, y0, y1, it, b = True):
    alls = [b:= b & (curr > z) for z in [map[y][x] for y in range(y0,y1,it) for x in range(x0,x1,it)]]
    return results[0] | all(alls), results[1] * (1 + sum([int(x) for x in alls]) - (bool(alls) and alls[-1]))

def ProcessTrees(x,y):
    res = PT(map[y][x], PT(map[y][x],(False, 1), x, x+1, y+1, len(map), 1), x+1, len(map[0]), y, y+1, 1)
    return PT(map[y][x], PT(map[y][x], res, x-1, -1, y, y-1, -1), x, x-1, y-1, -1, -1)

results = [ProcessTrees(x,y) for y in range(len(map)) for x in range(len(map[0]))]
print("Part1: {} | Part2: {}".format(sum([x[0] for x in results]),max([x[1] for x in results])))
import time
import heapq
from collections import defaultdict
from multiprocessing import Process, Array

class Ctx:
    def __init__(self, gScore, heap, cameFrom, end, map, invalidators):
        self.gScore = gScore
        self.heap = heap
        self.cameFrom = cameFrom
        self.end = end
        self.map = map
        self.invalidators = invalidators

def Comp(current, offset, ctx):
    currentPos = current[1]
    neighbour = (currentPos[0] + offset[0], currentPos[1] + offset[1])
    if not (len(ctx.map[0]) > neighbour[0] >= 0 and len(ctx.map) > neighbour[1] >= 0): return
    if ord(ctx.map[neighbour[1]][neighbour[0]]) - ord(ctx.map[currentPos[1]][currentPos[0]]) > 1: return

    hist = ctx.gScore[currentPos] + 1
    if hist < ctx.gScore[neighbour]:
        ctx.cameFrom[neighbour] = currentPos
        ctx.gScore[neighbour] = hist
        ctx.invalidators[(current[0], current[1])] = False
        inv = Invalidator()
        dist = hist + abs(neighbour[0] - ctx.end[0]) + abs(neighbour[1] - ctx.end[1])
        heapq.heappush(ctx.heap, (dist, neighbour, inv))
        ctx.invalidators[(dist, neighbour)] = inv

class Invalidator: Value = True

def Calc(start, index, scores, end, map):
    cameFrom = dict()
    gScore = defaultdict(lambda: 9999999)
    gScore[start] = 0
    invalidators = dict()
    dist = abs(start[0] - end[0]) + abs(start[1] - end[1])
    inv = Invalidator()
    heap = [(dist, start, inv)]
    invalidators[(dist,start)] = inv
    ctx = Ctx(gScore, heap, cameFrom, end, map, invalidators)
    while heap:
        current = heapq.heappop(heap)       
        if current[2].Value == False: continue

        if current[1] == end:
            tmp = current[1]
            while tmp in cameFrom.keys():
                tmp = cameFrom[tmp]
                scores[index] += 1
            return
        Comp(current, (1,0), ctx)
        Comp(current, (0,1), ctx)
        Comp(current, (-1,0), ctx)
        Comp(current, (0,-1), ctx)
    scores[index] = 99999999

def CalcRange(starts, indexRange, scores, end, map):
    for i in range(indexRange[0], indexRange[1]):
        Calc(starts[i], i, scores, end, map)

if __name__ == "__main__":
    map = [x.strip() for x in open("input.txt").readlines()]
    sPos = (0,0)
    end = (0,0)
    starts = []
 
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'a': starts.append((j, i))
        if 'S' in map[i]:
            starts.insert(0, (map[i].index('S'), i))
            map[i] = map[i][:starts[0][0]] + 'a' + map[i][starts[0][0]+1:]
        if 'E' in map[i]:
            end = (map[i].index('E'), i)
            map[i] = map[i][:end[0]] + 'z' + map[i][end[0]+1:]

    start = time.time()
    threadsAmount = 20
    threads = []
    scores = Array('i', (len(starts)))
    perThread = int(len(starts) / (threadsAmount - 1)) if threadsAmount > 1 else 0
    rest = len(starts) % (threadsAmount - 1) if threadsAmount > 1 else len(starts)
    for i in range(0,threadsAmount-1):
        threads.append(Process(target=CalcRange, args=(starts, (rest + i * perThread, rest + (i + 1) * perThread), scores,end,map)))
        threads[-1].start()  

    CalcRange(starts, (0, rest), scores, end, map)

    for thread in threads:
        thread.join()

    print(scores[0])
    print(min(scores))
    print(time.time() - start)
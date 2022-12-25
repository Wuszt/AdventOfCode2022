from collections import defaultdict
import heapq

level = [x.strip() for x in open("input.txt").readlines()]

initialBlizzards = dict()
for y in range(len(level)):
    for x in range(len(level[y])):
        if level[y][x] == '<' or level[y][x] == '>' \
            or level[y][x] == 'v' or level[y][x] == '^':
            initialBlizzards[(x,y)] = level[y][x]
            level[y] = level[y][:x] + '.' + level[y][x+1:]

blizzards = [initialBlizzards]
def GetBlizzard(r):
    for i in range(len(blizzards)-1, r+1):
        tmp = defaultdict(list)
        for cell,arr in blizzards[-1].items():
            for c in arr:
                x = 0
                y = 0
                if c == '<':
                    x = -1
                elif c == '>':
                    x = 1
                elif c == '^':
                    y = -1
                elif c == "v":
                    y = 1
                x = cell[0] + x
                y= cell[1] + y
                x = (x - 1 + len(level[0]) - 2) % (len(level[0]) - 2) + 1
                y = (y - 1 + len(level) - 2) % (len(level) - 2) + 1
                tmp[(x,y)].append(c)
        blizzards.append(tmp)
    return blizzards[r]

def DrawLevel(r):
    for y in range(len(level)):
        for x in range(len(level[y])):
            if (x,y) in blizzards[r]:
                if len(blizzards[r][(x,y)]) > 1:
                    print(len(blizzards[r][(x,y)]), end ="")
                else:
                    print(blizzards[r][(x,y)][0], end="")
            else:
                print(level[y][x], end="")
        print()
    print()

start = (1,0)
end = (len(level[0])-2, len(level)-1)

def GetMoves(cp):
    return [(cp[0] + 1, cp[1]), (cp[0] - 1, cp[1]), cp, (cp[0],cp[1]+1), (cp[0], cp[1]-1)]

def CalcScore(move, minute, end):
    return abs(move[0]-end[0]) + abs(move[1] - end[1]) + minute

def Process(start, end, r):
    openSet = set()
    heap = []
    openSet.add((start, r))
    heap.append((0,(start,r)))
    while openSet:
        move = heapq.heappop(heap)[1]
        if move[0] == end:
            return move[1]

        openSet.remove(move)
        moves = GetMoves(move[0])
        nextMinute = move[1] + 1
        for m in moves:
            if m not in GetBlizzard(nextMinute):
                if m[1] >= 0 and m[1] < len(level):
                    if level[m[1]][m[0]] != '#':
                        if (m,nextMinute) not in openSet:
                            openSet.add((m, nextMinute))
                            heapq.heappush(heap, (CalcScore(m, nextMinute, end), (m,nextMinute)))

first = Process(start, end,0)
print(first)
second = Process(end, start, first) - first
print(second)
third = Process(start, end, first + second) - first - second
print(third)

print("Result:" + str(first+second+third))
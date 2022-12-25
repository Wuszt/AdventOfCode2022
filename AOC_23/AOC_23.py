from collections import defaultdict

raw = open("input.txt").readlines()
mins= (0,0)
maxs = (len(raw[0])-1,len(raw)-1)

elves = set()
for y in range(len(raw)):
    for x in range(len(raw[y])):
        if raw[y][x] == '#':
            elves.add((x,y))

def Add(l,r): return (l[0] + r[0], l[1] + r[1])

moves = \
    [
        lambda elf: Add(elf, (-1,-1)),
        lambda elf: Add(elf, (0,-1)),
        lambda elf: Add(elf, (1,-1)),
        lambda elf: Add(elf, (-1,0)),
        lambda elf: Add(elf, (1,0)),
        lambda elf: Add(elf, (-1,1)),
        lambda elf: Add(elf, (0,1)),
        lambda elf: Add(elf, (1,1))
    ]

movesList = \
    [
        [0,1,2],
        [5,6,7],
        [0,3,5],
        [2,4,7]
    ]

dirs = \
    [
        lambda elf: Add(elf, (0,-1)),
        lambda elf: Add(elf, (0,1)),
        lambda elf: Add(elf, (-1,0)),
        lambda elf: Add(elf, (1,0))
    ]


def Draw():
     for y in range(mins[1], maxs[1]+1):
         for x in range(mins[0], maxs[0]+1):
             if (x,y) in elves:
                 print('#', end ='')
             else:
                 print('.', end='')
         print()
     print()

for r in range(999999):
    #Draw()
    commonMoves = defaultdict(int)
    elvesMoves = dict()
    newElves = set()
    for elf in elves:
        allClear = True
        for i in range(4):
            moveIndex = (r + i) % 4
            movesIndices = movesList[moveIndex]
            for index in movesIndices:
                allClear &= moves[index](elf) not in elves

        if allClear:
            newElves.add(elf)
            continue

        anyClear = False
        for i in range(4):
            moveIndex = (r + i) % 4
            movesIndices = movesList[moveIndex]
            allClear = True
            for index in movesIndices:
                allClear &= moves[index](elf) not in elves
            if allClear:
                elvesMoves[elf] = dirs[moveIndex](elf)
                commonMoves[dirs[moveIndex](elf)] += 1
                anyClear = True
                break
        if not anyClear:
            newElves.add(elf)

    if len(elves) == len(newElves):
        print(r+1)
        break

    elves = newElves
    for key,value in elvesMoves.items():
        if commonMoves[value] == 1:
            elves.add(value)
        else:
            elves.add(key)

    mins = (99999,99999)
    maxs = (-99999,-99999)
    for elf in elves:
        mins = (min(elf[0], mins[0]), min(elf[1], mins[1]))
        maxs = (max(elf[0], maxs[0]), max(elf[1], maxs[1]))

#Draw()

counter = 0
for y in range(mins[1], maxs[1]+1):
    for x in range(mins[0], maxs[0]+1):
        if (x,y) not in elves:
            counter += 1
print(counter)

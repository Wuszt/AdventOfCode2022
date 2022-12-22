cubes = [tuple([int(y) for y in x.strip().split(',')]) for x in open("input.txt").readlines()]

surface = 6 * len(cubes)

cubesSet = set(cubes)

mins = (999999,999999,999999)
maxs = (0,0,0)
for cube in cubes:
    mins = (min(mins[0], cube[0]), min(mins[1], cube[1]), min(mins[2], cube[2]))
    maxs = (max(maxs[0], cube[0]), max(maxs[1], cube[1]), max(maxs[2], cube[2]))

airs = set()
for x in range(mins[0],maxs[0]):
    for y in range(mins[1],maxs[1]):
        for z in range(mins[2],maxs[2]):
            if (x,y,z) not in cubesSet:
                airs.add((x,y,z))

def AreNeighbours(cube0, cube1):
    f = abs(cube0[0] - cube1[0])
    f += abs(cube0[1] - cube1[1])
    f += abs(cube0[2] - cube1[2])
    return f == 1

for i in range(len(cubes)):
    current = cubes[i]
    for j in range(i + 1, len(cubes)):
        tmpCube = cubes[j]
        if AreNeighbours(current, tmpCube):
            surface -= 2

def TryToAdd(cube, openList, visitedList):
    if cube not in openList and cube not in visitedList and cube not in cubesSet:
        openList.add(cube)

    if cube in cubesSet:
        return 1

    return 0

def Traverse(openList, visited):
    counter = 0
    while openList:
        current = openList.pop()

        visited.add(current)

        if mins[0] >= current[0] or current[0] >= maxs[0] \
        or mins[1] >= current[1] or current[1] >= maxs[1] \
        or mins[2] >= current[2] or current[2] >= maxs[2]:
            return 0

        counter += TryToAdd((current[0] + 1, current[1], current[2]), openList, visited)
        counter += TryToAdd((current[0] - 1, current[1], current[2]), openList, visited)
        counter += TryToAdd((current[0], current[1] + 1, current[2]), openList, visited)
        counter += TryToAdd((current[0], current[1] - 1, current[2]), openList, visited)
        counter += TryToAdd((current[0], current[1], current[2] + 1), openList, visited)
        counter += TryToAdd((current[0], current[1], current[2] - 1), openList, visited)
    return counter

while airs:
    air = airs.pop()
    visited = set()
    openList = {air}
    surface -= Traverse(openList, visited)
    airs -= openList
    airs -= visited

print(surface)
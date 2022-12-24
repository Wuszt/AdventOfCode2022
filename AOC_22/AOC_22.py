#myMap = open("input.txt").readlines()
#rawInstructions = myMap[-1].strip()
#myMap = myMap[:-2]

#width = max([len(x) for x in myMap]) - 1

#widths = []
#offsetsX = []

#for i in range(len(myMap)):
#    myMap[i] = myMap[i].replace('\n', '')
#    widths.append(len(myMap[i].strip()))
#    offsetsX.append(len(myMap[i].rstrip()) - widths[-1])
#    myMap[i] = myMap[i].ljust(width, ' ')

#heights = []
#offsetsY = []
#for w in range(width):
#    offsetsY.append(0)
#    heights.append(0)
#    for y in range(len(myMap)):
#        if myMap[y][w] == ' ':
#            if heights[-1] > 0:
#                break
#            offsetsY[-1] += 1
#        else:
#            heights[-1] += 1

#currentPos = (myMap[0].find('.'),0)
#dir = 0
#dirs = [(1,0),(0,1),(-1,0),(0,-1)]

#i = 0
#instructions = []
#while i < len(rawInstructions):
#    number = []
#    turn = 0
#    for j in range(i,len(rawInstructions)):
#        if rawInstructions[j].isdigit():
#            number.append(rawInstructions[j])
#        else:
#            turn = 1 if rawInstructions[j] == 'R' else -1
#            break
#    instructions.append((int("".join(number)), turn))
#    i += len(number) + 1

#for instruction in instructions:
#    for i in range(instruction[0]):
#        nextX = currentPos[0] + dirs[dir][0]
#        nextY = currentPos[1] + dirs[dir][1]
        
#        if dirs[dir][0] != 0:
#            nextX = offsetsX[nextY] + (nextX - offsetsX[nextY] + widths[nextY]) % widths[nextY]   
#        else:
#            nextY = offsetsY[nextX] + (nextY - offsetsY[nextX] + heights[nextX]) % heights[nextX]      

#        if myMap[nextY][nextX] == '#':
#            break

#        row = myMap[nextY]
#        myMap[nextY] = row[:nextX] + 'O' + row[nextX+1:]

#        currentPos = (nextX, nextY)

#    dir = (dir + instruction[1] + 4) % 4

#column = currentPos[0] + 1
#row = currentPos[1] + 1
#print(row *1000 + column * 4 + dir)

spaces = [len(x) - len(x.strip()) - 1 for x in open("input.txt").readlines()[:-2]]

myMap = [x.strip() for x in open("input.txt").readlines()]
rawInstructions = myMap[-1].strip()
myMap = myMap[:-2]

i = 0
instructions = []
while i < len(rawInstructions):
    number = []
    turn = 0
    for j in range(i,len(rawInstructions)):
        if rawInstructions[j].isdigit():
            number.append(rawInstructions[j])
        else:
            turn = 1 if rawInstructions[j] == 'R' else -1
            break
    instructions.append((int("".join(number)), turn))
    i += len(number) + 1

sideSize = 50
sidesPos = [(0,0), (sideSize,0),(0,sideSize), (0,sideSize*2), (sideSize,sideSize*2),(0,sideSize*3)]

sidesPortals = \
    [
        [lambda x,y: (0, y, 1, 0), lambda x,y: (x,0, 2, 1), lambda x,y: (0,sideSize - 1 - y, 3, 0), lambda x,y: (0,x, 5, 0)],
        [lambda x,y: (sideSize - 1, sideSize-1-y,4, 2), lambda x,y:(sideSize-1, x, 2, 2), lambda x,y: (sideSize-1,y,0,2), lambda x,y: (x,sideSize-1,5,3)],
        [lambda x,y: (y, sideSize - 1, 1, 3), lambda x,y: (x, 0, 4, 1), lambda x,y: (y, 0, 3, 1), lambda x,y: (x, sideSize-1,0,3)],
        [lambda x,y: (0, y, 4, 0), lambda x,y: (x, 0, 5, 1), lambda x,y: (0, sideSize- 1-y, 0,0), lambda x,y: (0, x, 2, 0)],
        [lambda x,y: (sideSize-1, sideSize-1-y,1, 2), lambda x,y: (sideSize-1, x, 5, 2), lambda x,y: (sideSize-1, y, 3, 2), lambda x,y: (x, sideSize-1, 2, 3)],
        [lambda x,y: (y, sideSize-1, 4, 3), lambda x,y: (x, 0, 1, 1), lambda x,y: (y, 0, 0, 1), lambda x,y: (x, sideSize-1, 3,3)]
    ]

dirs = [(1,0),(0,1),(-1,0),(0,-1)]

import random
for i in range(0,1):
    testPos = (random.randint(0, sideSize-1), random.randint(0, sideSize-1), random.randint(0, 5))
    currentPos = testPos
    dir = random.randint(0,3)
    for j in range(0,4*sideSize):
        nextX = currentPos[0] + dirs[dir][0]
        nextY = currentPos[1] + dirs[dir][1]

        outcome = (nextX, nextY, currentPos[2], dir)

        portals = sidesPortals[currentPos[2]]

        if nextX >= sideSize:
            outcome = portals[0](nextX, nextY)
        elif nextX < 0:
            outcome = portals[2](nextX, nextY)

        if nextY >= sideSize:
            outcome = portals[1](nextX, nextY)
        elif nextY < 0:
            outcome = portals[3](nextX, nextY)

        currentPos = (outcome[0], outcome[1], outcome[2])
        dir = outcome[3]
    if currentPos[0] != testPos[0] or currentPos[1] != testPos[1]:
        dir = dir
dir = dir
        
currentPos = (0,0,0)
dir = 0
for instruction in instructions:
    for i in range(instruction[0]):
        nextX = currentPos[0] + dirs[dir][0]
        nextY = currentPos[1] + dirs[dir][1]

        outcome = (nextX, nextY, currentPos[2], dir)

        portals = sidesPortals[currentPos[2]]

        if nextX >= sideSize:
            outcome = portals[0](nextX, nextY)
        elif nextX < 0:
            outcome = portals[2](nextX, nextY)

        if nextY >= sideSize:
            outcome = portals[1](nextX, nextY)
        elif nextY < 0:
            outcome = portals[3](nextX, nextY)

        offset = sidesPos[outcome[2]]
        if myMap[offset[1] + outcome[1]][offset[0] + outcome[0]] == '#':
            break

        nextX = outcome[0]
        nextY = outcome[1]

        row = myMap[nextY + offset[1]]
        chars = ['>', 'v', '<', '^']

        myMap[nextY + offset[1]] = row[:nextX+offset[0]] + chars[dir] + row[nextX+offset[0]+1:]

        #for row in myMap:
        #    print(row)

        currentPos = (outcome[0], outcome[1], outcome[2])
        dir = outcome[3]
    dir = (dir + instruction[1] + 4) % 4

offset = sidesPos[currentPos[2]]
row = offset[1] + currentPos[1] + 1
column = offset[0] + spaces[row-1] + currentPos[0] + 1
print(row *1000 + column * 4 + dir)

#for row in myMap:
#    print(row)

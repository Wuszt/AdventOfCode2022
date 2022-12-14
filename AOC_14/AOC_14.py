rows = [x.split()[0::2] for x in open("input.txt").readlines()]
rows = [[[int(z) for z in x.split(',')] for x in y] for y in rows]
minX = min(min([y[0] for x in rows for y in x]),500)
maxX = max(max([y[0] for x in rows for y in x]),500)
minY = min(min([y[1] for x in rows for y in x]),0)
maxY = max(max([y[1] for x in rows for y in x]),0)

offset = maxY - minY + 2 - minX
map = [['.' for _ in range(maxX + minX + offset * 2)] for _ in range(maxY + 3)]
rows = [[(y[0]+offset, y[1]) for y in x] for x in rows]

for row in rows:
    for i in range(1,len(row)):
        diff = (row[i][0] - row[i-1][0], row[i][1] - row[i-1][1])
        for x in range(abs(diff[0]) + 1):
            map[row[i][1]][(row[i][0] if row[i][0] < row[i-1][0] else row[i-1][0]) + x] = '#'
        for y in range(abs(diff[1]) + 1):
            map[(row[i][1] if row[i][1] < row[i-1][1] else row[i-1][1]) + y][row[i][0]] = '#'

part1_result = 999999
counter = 0
while True:
    pos = (500 + offset, 0)
    counter += 1
    if map[0][500 + offset] != '.': break
    while True:
        poses = [(pos[0], pos[1] + 1), (pos[0] -1, pos[1] + 1), (pos[0] + 1, pos[1] + 1)]
        if pos[1] >= maxY + 1: break
        elif map[poses[0][1]][poses[0][0]] == '.': pos = poses[0]          
        elif map[poses[1][1]][poses[1][0]] == '.': pos = poses[1]          
        elif map[poses[2][1]][poses[2][0]] == '.': pos = poses[2]
        else: break
        if pos[1] >= maxY: part1_result = min(part1_result, counter-1)       
    map[pos[1]][pos[0]] = 'O'

for row in map: print("".join(row))
print("Part1: {} | Part2: {}".format(str(part1_result), str(counter-1)))
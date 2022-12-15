import time
lines = open("input.txt").readlines()
sensors = []
beacons = set()

for line in lines:
    a = line.split()
    x0 = int(a[2].split('=')[1].split(',')[0])
    y0 = int(a[3].split('=')[1].split(':')[0])
    x1 = int(a[8].split('=')[1].split(',')[0])
    y1 = int(a[9].split('=')[1])
    beacons.add((x1,y1,0))
    sensors.append((x0,y0,abs(x0 - x1) + abs(y0 - y1)))

def Part1():
    counter = 0
    y = 2000000
    part1Sensors = [sensor for sensor in (sensors + list(beacons)) if sensor[2] >= abs(sensor[1] - y)]
    minX = min([sensor[0] - (sensor[2] - abs(sensor[1] - y)) for sensor in part1Sensors])
    maxX = max([sensor[0] + (sensor[2] - abs(sensor[1] - y)) for sensor in part1Sensors])

    x = minX
    while x < maxX:
        for i in range(len(part1Sensors)):
            sensor = part1Sensors[i]
            yDist = abs(sensor[1] - y)
            if abs(sensor[0] - x) + yDist <= sensor[2]:
                newX = sensor[0] + sensor[2] - yDist
                counter += newX - x + 1
                x = newX
                del part1Sensors[i]
                break
        x += 1
    counter -= sum([int(s[1] == y) for s in part1Sensors])
    print(counter)
    counter = counter

def Part2():
    start = time.time()
    searchRange = 4000000
    localSensors = [(sensor[0], sensor[1], sensor[2], (sensor[1] - sensor[2], sensor[1] + sensor[2])) for sensor in sensors]
    for y in range(searchRange):
        x = 0
        part2Sensors = [(sensor[0], abs(sensor[1] - y), sensor[2]) for sensor in localSensors if sensor[3][0] <= y <= sensor[3][1]]
        while x < searchRange:
            for i in range(len(part2Sensors)):
                if abs(part2Sensors[i][0] - x) + part2Sensors[i][1] <= part2Sensors[i][2]:
                    x = part2Sensors[i][0] - part2Sensors[i][1] + part2Sensors[i][2] 
                    part2Sensors[i] = part2Sensors[-1]
                    part2Sensors.pop()
                    break
            else:
                print(str((x,y)))
                print(x * searchRange + y)
                print(time.time() - start)
                exit()
            x+=1

Part1()
Part2()

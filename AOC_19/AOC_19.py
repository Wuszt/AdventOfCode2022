import time
index = 1

part2 = True
result = 1 if part2 else 0
duration = 32 if part2 else 24

for line in open("input.txt"):
    nrs = [int(x) for x in line.split() if x.isdigit()]
    costs = [[nrs[0],0,0,0],[nrs[1],0,0,0],[nrs[2],nrs[3],0,0],[nrs[4], 0, nrs[5], 0]]
    resources = (0,0,0,0)
    robots = (1,0,0,0)
        
    bestScore = 0
    bestRobots = tuple()
    bestResources = tuple()

    highestCosts = [max([x[i] for x in costs]) for i in range(4)]

    cacheSize = 100000000
    cache = [False] * cacheSize

    def CalcHash(minute, resources, robots):
        return hash((minute, resources, robots))       

    import math
    def Div(a,b):
        if a == 0: return 0
        if b == 0: return 99999
        return math.ceil(a/b)

    def Simulate(minute, resources, robots):
        global costs, bestScore, bestRobots, bestResources
        key = CalcHash(minute, resources, robots)
        if cache[key % cacheSize]:
            return

        cache[key % cacheSize] = True

        toEnd = duration - minute
        if resources[3] + (robots[3] + toEnd) * toEnd <= bestScore:
            return

        if minute == duration:
            if resources[3] > bestScore:
                bestScore = resources[3]
                bestResources = resources
                bestRobots = robots
            return

        for i in range(len(resources)):
            if (robots[i] >= highestCosts[i] and i != 3):
                continue

            newResources = tuple(map(int.__sub__,resources, costs[i]))
            diff = tuple(map(min, newResources, (0,0,0,0)))
            diff = tuple(map(abs, diff))

            stepMinutes = 1
            fastExit = False
            for d in range(len(diff)):
                if diff[d] > 0 and robots[d] == 0:
                    fastExit = True
                    break
                if robots[d] != 0:
                    stepMinutes = max(stepMinutes, math.ceil(diff[d] / robots[d]) + 1)

            if not fastExit and minute + stepMinutes <= duration:
                rob = tuple(map(int.__mul__,robots, [stepMinutes] * len(robots)))
                newResources = tuple(map(int.__add__, rob, newResources))
                lrobots = list(robots)
                lrobots[i] += 1
                Simulate(minute + stepMinutes, newResources, tuple(lrobots))


    start = time.time()
    Simulate(0, resources, robots)
    print(time.time() - start)
    if part2:
        result *= bestScore
        if index >= 3:
            break
    else:
        result += index * bestScore
    index+=1
print(result)
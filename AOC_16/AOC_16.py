class Valve:
    connections = dict()
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

valves = dict()
lines = [x.split() for x in open("input.txt").readlines()]
for line in lines:
    name = line[1]
    rawRate = line[4]
    rate = int(rawRate[5:-1])
    valves[name] = Valve(name, rate)

for line in lines:
    name = line[1]
    tmp = line[9:]
    tmp = [x.replace(',', '') for x in tmp]
    valves[name].connections = {valves[x]:1 for x in tmp }

connections = dict()

def Dijkstra(source):
    dist = { valves[x]:float("inf") for x in valves }
    prev = { valves[x]:None for x in valves }
    queue = list(valves.values())
    dist[source] = 0

    while queue:
        u = queue[0]
        for q in queue:
            if dist[u] > dist[q]:
                u = q
        queue.remove(u)

        for dest, d in u.connections.items():
            if dest in queue:
                alt = dist[u] + d
                if alt < dist[dest]:
                    dist[dest] = alt
                    prev[dest] = u

    return dist

bestPath = []
bestElephantPath = []

myPath = []
elephantPath = []
openValves = set([x for x in valves.values() if x.rate > 0 ])

for valve in valves.values():
    valve.connections = Dijkstra(valve)

bestScore = 0

def Calc(currentMe, currentEl, score, myTimeLeft, elTimeLeft, isElephantTurn):
    global bestScore, bestPath, bestElephantPath

    if elTimeLeft <= 0 and myTimeLeft <= 0:
        return

    if elTimeLeft <= 0:
        isElephantTurn = False
    elif myTimeLeft <= 0:
        isElephantTurn = True

    if score > bestScore:
        bestScore = score
        bestElephantPath = elephantPath.copy()
        bestPath = myPath.copy()

    if isElephantTurn:
        current = currentEl
        path = elephantPath
        timeLeft = elTimeLeft
    else:
        current = currentMe
        path = myPath
        timeLeft = myTimeLeft

    for valve in openValves:
        openValves.remove(valve)
        path.append(valve)
        tmpTimeLeft = timeLeft - current.connections[valve] - 1
        if tmpTimeLeft > 0:
            tmpScore = score + valve.rate * tmpTimeLeft
            if isElephantTurn:
                Calc(currentMe, valve, tmpScore, myTimeLeft, tmpTimeLeft, False)
            else:
                Calc(valve, currentEl, tmpScore, tmpTimeLeft, elTimeLeft, True)
        path.pop()
        openValves.add(valve)

Calc(valves["AA"], valves["AA"], 0, 26, 26, False)
print(bestScore)
print("Elephant:" + str([x.name for x in bestElephantPath]))
print("Me:" + str([x.name for x in bestPath]))
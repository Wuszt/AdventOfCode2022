### Part1
#from collections import defaultdict
#results = dict()
#callbacks = defaultdict(list)
#waiting = dict()

#for line in open("input.txt"):
#    splitted = line.strip().split()
#    name = splitted[0][:-1]
#    if len(splitted) == 2:
#        results[name] = splitted[1]
#    else:
#        waiting[name] = (splitted[1], splitted[2], splitted[3])
#        callbacks[splitted[1]].append(name)
#        callbacks[splitted[3]].append(name)

#def TryToCalculate(name):
#    if name not in waiting:
#        return

#    if waiting[name][0] not in results:
#        return

#    if waiting[name][2] not in results:
#        return

#    left = results[waiting[name][0]]
#    right = results[waiting[name][2]]
#    result = eval(left + waiting[name][1] + right)
#    results[name] = str(result)
#    for callback in callbacks[name]:
#        TryToCalculate(callback)
#    del waiting[name]

#initialResults = list(results.keys())
#for key in initialResults:
#    for callback in callbacks[key]:
#        TryToCalculate(callback)

#print(results["root"])
###

###Part2
from collections import defaultdict

i = 0
step = 10000000000000
prevDiff = 9999999999999
sign = 1

iterations = 0

while True:
    iterations += 1
    results = dict()
    callbacks = defaultdict(list)
    waiting = dict()
    root = tuple()

    for line in open("input.txt"):
        splitted = line.strip().split()
        name = splitted[0][:-1]
        if name == "root":
            root = (splitted[1], splitted[3])
        elif len(splitted) == 2:
            if name == "humn":
                results[name] = str(i)
            else:
                results[name] = splitted[1]
        else:
            waiting[name] = (splitted[1], splitted[2], splitted[3])
            callbacks[splitted[1]].append(name)
            callbacks[splitted[3]].append(name)

    def TryToCalculate(name):
        if name not in waiting:
            return

        if waiting[name][0] not in results:
            return

        if waiting[name][2] not in results:
            return

        left = results[waiting[name][0]]
        right = results[waiting[name][2]]
        result = eval(left + waiting[name][1] + right)
        results[name] = str(result)
        for callback in callbacks[name]:
            TryToCalculate(callback)
        del waiting[name]

    initialResults = list(results.keys())
    for key in initialResults:
        for callback in callbacks[key]:
            TryToCalculate(callback)

    left = float(results[root[0]])
    right = float(results[root[1]])

    if left == right:
        break

    diff = right - left
    if (prevDiff > 0) == (diff > 0):
        if abs(prevDiff) < abs(diff):
            sign = -sign

        i += sign * step
        step = int(step * 1.5)
    else:
        step = max(1, int(step/2))
        sign = -sign
        i += sign * step

    prevDiff = diff
print("{} in {} iterations".format(i, iterations))
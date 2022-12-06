def Compute(msgLength):
    data = open("input.txt").readlines()[-1]
    for i in range(msgLength, len(data)):
        if len(set(data[i-msgLength:i])) == msgLength:
            return str(i)

print("Part1: " + (Compute(4) + " | Part2: " + Compute(14)))
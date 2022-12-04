file = open("input.txt", "r")
counters = (0,0)
for line in file:
    ranges = [[int(y) for y in x.split('-')] for x in line.strip().split(',') ]
    counters = (counters[0] + ((ranges[0][0] - ranges[1][0]) * (ranges[1][1] - ranges[0][1]) >= 0), counters[1])
    counters = (counters[0], counters[1] + ((ranges[1][0] - ranges[0][1]) * (ranges[0][0] - ranges[1][1]) >= 0))
print("Part1: " + str(counters[0]) + " | Part2: " + str(counters[1]))
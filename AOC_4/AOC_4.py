xs = [line.strip().split(',') for line in open("input.txt", "r")]
rs = [[[int(y) for y in z.split('-')] for z in x] for x in xs]
print(sum([(r[0][0]-r[1][0]) * (r[1][1]-r[0][1]) >= 0 for r in rs]))
print(sum([(r[1][0]-r[0][1]) * (r[0][0]-r[1][1]) >= 0 for r in rs]))
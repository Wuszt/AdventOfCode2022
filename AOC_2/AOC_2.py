def Part1_CalcPoints(opponent, me):
	meNum = ord(me) - ord("X")
	return meNum + 1 + ((meNum + 4 - (ord(opponent) - ord("A"))) % 3) * 3

def Part2_CalcPoints(opponent, me):
	meNum = (ord(me) - ord("X") + 2) % 3
	return (ord(opponent) - ord("A") + meNum) % 3 + 1 + (meNum + 1) % 3 * 3

file = open("input.txt", "r")
results = (0,0)
for line in file:
	opponent = line.split(" ")[0].strip()
	me = line.split(" ")[1].strip()
	results = (results[0] + Part1_CalcPoints(opponent, me), results[1] + Part2_CalcPoints(opponent, me))

print(results[0])
print(results[1])

def CalcScoreOfCommons(substrings):
	duplicates = set(substrings[0])

	for substr in substrings:
		duplicates = duplicates&set(substr)

	score = 0
	for d in duplicates:
		if d.isupper():
			score += 26
		score += ord(d.lower()) - ord('a') + 1
	return score

file = open("input.txt", "r")
lines = []
sums = (0,0)
for line in file:
	line = line.strip()
	sums = (sums[0] + CalcScoreOfCommons([line[:int(len(line) / 2)],line[int(len(line) / 2):]]), sums[1])
	lines.append(line)
	if(len(lines) == 3):
		sums = (sums[0], sums[1] + CalcScoreOfCommons(lines))
		lines = []
print("Part1: " + str(sums[0]) + " | Part2: " + str(sums[1]))
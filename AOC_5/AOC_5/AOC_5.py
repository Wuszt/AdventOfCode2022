import re
def Compute(isCrateMover9001):
    with open("input.txt") as file:
        lines = file.readlines()
        index = lines.index('\n')
        rawStack, rawInstructions = lines[:index - 1], lines[index + 1:]

    stacks = [[] for _ in range(int(len(rawStack[0]) / 4))]
    for line in rawStack:
        for i in range(len(stacks)):
            el = line[i * 4 + 1].strip()
            if el: stacks[i].insert(0, el)

    for instruction in [[int(y) for y in x] for x in [re.findall(r'\d+',raw) for raw in rawInstructions]]:    
        buff = []
        for i in range(instruction[0]):
            buff.append(stacks[instruction[1] - 1].pop())
        stacks[instruction[2] - 1] += buff[::-1] if isCrateMover9001 else buff

    return "".join([x[-1] for x in stacks])

print("Part1: " + Compute(False) + " | Part2: " + Compute(True))
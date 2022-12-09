cmds = [x.strip().split() for x in open("input.txt").readlines()]
grid = set()
KNOTS_AMOUNT = 9
nodes = [[0,0] for _ in range(0,KNOTS_AMOUNT + 1)]
for cmd in cmds:
    dir = [0,0]
    if cmd[0] == 'L': dir[0] = -1
    elif cmd[0] == 'R': dir[0] = 1
    if cmd[0] == 'U': dir[1] = 1
    elif cmd[0] == 'D': dir[1] = -1
    for i in range(int(cmd[1])):
        nodes[0] = [nodes[0][0] + dir[0], nodes[0][1] + dir[1]]
        for i in range(1,len(nodes)):
            diff = [nodes[i-1][0] - nodes[i][0], nodes[i-1][1] - nodes[i][1]]
            if max(abs(diff[0]), abs(diff[1])) > 1:
                nodes[i][0] += (diff[0] / max(1,abs(diff[0])))
                nodes[i][1] += (diff[1] / max(1,abs(diff[1])))        
        grid.add((nodes[-1][0],nodes[-1][1]))
print(len(grid))
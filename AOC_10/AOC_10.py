with open("input.txt") as file:
    spritePos, part1_res = 1, 0
    nextCmd = [0,0]
    screen = [['.'] * 40 for _ in range(6)]
    for CRT in range(240):
        if CRT%40 == 20: part1_res += CRT * spritePos
        if CRT == nextCmd[0]:
            spritePos += nextCmd[1]
            line = file.readline().strip().split()
            if line[0] == 'noop': nextCmd = [CRT + 1, 0]
            else: nextCmd = [CRT + 2,int(line[1])]
        if spritePos + 1 >= CRT%40 >= spritePos - 1:
            screen[int(CRT/40)][CRT%40] = '#'

    print(part1_res)
    for row in screen: print(''.join(row))
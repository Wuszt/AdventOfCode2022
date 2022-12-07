dirsSizes = []
lines = open("input.txt")

def ParseDir():
    size = 0
    file.readline()
    for line in file:
        if line[0] == '$':
            if line.split()[2] == "..":
                break
            size += ParseDir()
        fileSize = line.split()[0]
        if fileSize.isnumeric(): size += int(fileSize)
    dirsSizes.append(size)
    return size

file.readline()
ParseDir()
print(sum([size for size in dirsSizes if size < 100000]))
dirsSizes.sort()
print(next(x for x in dirsSizes if x > dirsSizes[-1] - 40000000))
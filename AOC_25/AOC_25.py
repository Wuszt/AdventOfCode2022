import math
mapping = {'2':2, '1':1, '0':0, '-':-1,'=':-2}
reversedMapping = {value:key for key,value in mapping.items()}

def toDec(txt):
    nr = 0
    for i in range(len(txt)):
        mult = mapping[txt[i]]
        nr += math.pow(5, len(txt)-i-1) * mult
    return nr

sum = 0
for line in open("input.txt"):
    line = line.strip()
    sum += toDec(line)

buff = []
for i in range(int(math.log(sum,5)),-1,-1):
    tmp = int(sum / math.pow(5,i))
    sum -= tmp * math.pow(5,i)
    buff.append(tmp)

converted = []
b = 0
for i in range(len(buff)-1, -1,-1):
    s = buff[i] + b
    b = 0
    if s > 2:
        b = 1
        s -= 5
    converted.insert(0, s)
if b > 0:
    converted.insert(0, b)

converted = [reversedMapping[x] for x in converted]
print("".join(converted))
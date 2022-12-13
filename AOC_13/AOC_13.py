from functools import cmp_to_key
def IsArray(val): return hasattr(val, "__len__")
def ConvertToArray(val): return val if IsArray(val) else [val]
def Check(left, right):
    if not (IsArray(left) or IsArray(right)): return right - left
    left, right = ConvertToArray(left), ConvertToArray(right)
    for i in range(min(len(left), len(right))):
        outcome = Check(left[i], right[i])
        if outcome != 0: return outcome
    return len(right) - len(left)

rows = [eval(x.strip()) for x in open("input.txt").readlines() if len(x.strip()) > 0]
print(sum([(i/2 +1)* int(Check(rows[i], rows[i+1]) > 0) for i in range(0,len(rows) - 1,2)]))
rows = sorted(rows + [[[2]],[[6]]], key=cmp_to_key(Check), reverse=True)
print((rows.index([[2]]) + 1) * (rows.index([[6]]) + 1))
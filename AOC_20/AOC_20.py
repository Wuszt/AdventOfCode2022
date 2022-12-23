class Node:   
    def __init__(self, prev, next, value):
        self.Prev = prev
        self.Next = next
        self.Value = value

isPart2 = True

nodes = [Node(None, None, int(x)) for x in open("input.txt")]
amount = len(nodes)
for i in range(amount):
    nodes[i].Value = nodes[i].Value * (811589153 if isPart2 else 1)
    nodes[i].Next = nodes[(i + 1) % amount]
    nodes[i].Prev = nodes[(i - 1 + amount) % amount]

def Draw():
    for i in range(amount):
        if nodes[i].Value == 0:
            current = nodes[i]
            while True:
                print(current.Value, end=",")
                current = current.Next
                if current == nodes[i]:
                    break
            break
    print()
        

for i in range(10 if isPart2 else 1):
    for node in nodes:
        if node.Value == 0:
            continue
        node.Prev.Next = node.Next
        node.Next.Prev = node.Prev
        if node.Value < 0:
            current = node
            for i in range(abs(node.Value) % (amount - 1)):
                current = current.Prev
            node.Prev = current.Prev
            node.Next = current
            current.Prev.Next = node
            current.Prev = node
        else:
            current = node
            for i in range(node.Value % (amount-1)):
                current = current.Next
            node.Prev = current
            node.Next = current.Next
            current.Next.Prev = node
            current.Next = node

tmp = []
for i in range(amount):
    if nodes[i].Value == 0:
        current = nodes[i]
        while True:
            tmp.append(current.Value)
            current = current.Next
            if current == nodes[i]:
                break
        break

a = tmp[1000%amount]
b = tmp[2000%amount]
c = tmp[3000%amount]
print(a+b+c)
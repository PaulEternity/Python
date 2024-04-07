n, s = map(int, input().split())
node = []

for i in range(n, 0, -1):
    if s >= i:
        node.append(i)
        s -= i

for i in range(len(node), n + 1):
    node.append(i)

print(' '.join(map(str, node)))

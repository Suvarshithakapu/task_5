from collections import OrderedDict
n = int(input())
d = OrderedDict()
for _ in range(n):
    w = input()
    d[w] = d.get(w,0)+1
print(len(d))
print(*d.values())
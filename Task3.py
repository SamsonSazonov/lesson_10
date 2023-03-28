n = int(input())
d = dict()
for i in range(n):
    name, num = [str(k) for k in input().split()]
    num = int(num)
    d[name] = d.get(name, 0) + num

for name, num in sorted(d.items()):
    print(name, num)

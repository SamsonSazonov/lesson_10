a = input().split()
b = {}
for i in a:
    b[i] = b.get(i, 0) + 1
    print(b[i] - 1, end=' ')

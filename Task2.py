a=dict()
for i in range (int(input())):
    key,val=[s for s in input().split()]
    a[key]=val
    a[val]=key
print(a[input()])

def fun(x):
    a = -float('inf')
    b = float('inf')
    while x>0:
        a = max(a, x%10)
        b = min(b, x%10)
        x //= 10
    s = a*11 + b*7
    return str(s)[-2:]


n = int(input())
l = list(map(int, input().split()))
for i in range(n):
    l[i] = fun(l[i])


d = {}
for i in range(10):
    for j in range(2):
        d[(i,j)] = 0

for i in range(n):
    if i%2 == 0:
        d[(int(l[i][0]),1)] += 1
    else:
        d[(int(l[i][0]),0)] += 1

s = 0
p = {}

for i in range(10):
    p[i] = 0

for i in d.keys():
    if d[i] == 2:
        p[i[0]] += 1
    elif d[i] > 2:
        p[i[0]] += 2

for i in range(10):
    if p[i] > 2:
        s += 2
    else:
        s += p[i]

print(s,end="")
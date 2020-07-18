n = int(input())
g = list(input())
b = list(input())
c = 0
p = 0
i = 0
while len(g) > 0 and c < len(g)-i:
    if g[i] == b[0]:
        p += 1
        i += 1
        b.pop(0)
        c = 0
    else:
        b.append(b.pop(0))
        c += 1
print(n-p,end="")
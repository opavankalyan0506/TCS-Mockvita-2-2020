def fun(s,i,r,m):

    global l
    global d

    if i == len(l):
        return r

    if abs(2*s-sum(l)) < m:
        r = max(s,sum(l)-s)
        m = abs(2*s-sum(l))

    if (s,i,r,m) in d.keys():
        return d[(s,i,r,m)]
    d[(s,i,r,m)] = min(fun(s+l[i],i+1,r,m), fun(s,i+1,r,m))
    return d[(s,i,r,m)]



l = list(map(int, input().split()))
m = float('inf')
r = sum(l)
d = {}
k = fun(0,0,r,m)
print(k,end="")
def lds(a, n):
    lds = [0 for i in range(n)]
    lds[0] = 1
    for i in range(n):
        lds[i] = 1
        for j in range(i):
            if (lds[j] != 0 and a[i] % a[j] == 0):
                lds[i] = max(lds[i], lds[j] + 1)
    return max(lds)
a=[]
n=int(input())
a.append(n)
for i in range(n):
    a.append(int(input()))
print(lds(a, len(a)))
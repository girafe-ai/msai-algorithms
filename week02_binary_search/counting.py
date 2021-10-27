def counting_sort(x):
    N = len(x)
    M = max(x) + 1
    a = [0] * M
    for v in x:
        a[v] += 1
    res = []
    for i in range(M):
        for j in range(a[i]):
            res.append(i)
    return res


def counting_sort2(x):
    N = len(x)
    M = max(x) + 1
    c = [0] * M
    for v in x:
        c[v] += 1
    for i in range(1, M):
        c[i] += c[i - 1]
    print(c)
    res = [None] * N
    for i in range(N):
        position = c[x[i]] - 1
        res[position] = x[i]
        c[x[i]] -= 1
    return res


N = int(input())
x = list(map(int, input().split()))
x = counting_sort2(x)
print(' '.join(map(str, x)))
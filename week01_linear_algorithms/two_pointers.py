def find_pair(a, X):
    i = 0
    j = N - 1
    while i != j:
        if a[i] + a[j] < X:
            i += 1
        elif a[i] + a[j] > X:
            j -= 1
        else: # a[i] + a[j] == X
            return i, j
    return None


N, X = map(int, input().split())
a = list(map(int, input().split()))

pair = find_pair(a, X)
if pair is None:
    print(-1)
else:
    print(*pair)

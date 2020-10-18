input()
x = list(map(int, input().split()))
N = len(x)
for i in range(N - 1):
    i_min = i
    for j in range(i + 1, N):
        if x[i_min] > x[j]:
            i_min = j
    x[i], x[i_min] = x[i_min], x[i]
print(' '.join(map(str, x)))

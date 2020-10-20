input()
x = list(map(int, input().split()))
N = len(x)
for i in range(0, N - 1):
    for j in range(0, N - i - 1):
        if x[j] > x[j + 1]:
            x[j], x[j + 1] = x[j + 1], x[j]
print(' '.join(map(str, x)))

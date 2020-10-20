input()
x = list(map(int, input().split()))
N = len(x)
for i in range(1, N):
    key = x[i]
    j = i - 1
    while j >= 0 and key < x[j]:
        x[j + 1] = x[j]
        j -= 1
    x[j + 1] = key
print(' '.join(map(str, x)))
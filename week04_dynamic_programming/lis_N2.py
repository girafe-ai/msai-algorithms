def lis_n2(x):
    N = len(x)
    d = [0] * N
    d[0] = 1
    for i in range(1, N):
        # don't need to find j
        # Need just to calculate maxd:
        max_d = 0
        for j in range(i):
            if x[j] < x[i] and d[j] > max_d:
                max_d = d[j]
        d[i] = max_d + 1
    return max(d)


if __name__ == '__main__':
    N = int(input())
    x = list(map(int, input().split()))
    print(lis_n2(x))

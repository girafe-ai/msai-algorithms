from time import time


def stairs_dp(s):
    N = len(s)
    d = [None] * N
    d[0] = s[0]
    d[1] = s[1]
    for i in range(2, N):
        d[i] = min(d[i - 1], d[i - 2]) + s[i]
    return d[N - 1]


def stairs_rec(s):
    if len(s) <= 2:
        return s[-1]
    d1 = stairs_rec(s[1:]) + s[0]
    d2 = stairs_rec(s[2:]) + s[1]
    return min(d1, d2)


if __name__ == '__main__':
    N = int(input())
    s = list(map(int, input().split()))
    t1 = time()
    print(stairs_dp(s))
    t2 = time()
    print(stairs_rec(s))
    t3 = time()
    dp_time = t2 - t1
    rec_time = t3 - t2
    print(f'Naive: {rec_time:.8f} sec')
    print(f'DP: {dp_time:.8f} sec')

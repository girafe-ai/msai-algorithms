from math import log2, floor, ceil

inf = 10**9


class RMQSparseTable:
    def __init__(self, a):
        N = len(a)
        K = ceil(log2(N)) + 1

        self.ST = [[None] * N for k in range(K)]
        self.ST[0] = list(a)

        for k in range(1, K):
            for i in range(N):
                if i + 2 ** (k - 1) < N:
                    self.ST[k][i] = min(self.ST[k - 1][i],
                                        self.ST[k - 1][i + 2 ** (k - 1)])
                else:
                    self.ST[k][i] = self.ST[k - 1][i]
        for k in range(K):
            print(' '.join(map(str, self.ST[k])))

    def rmq(self, l, r):
        if l == r:
            return inf
        k = floor(log2(r - l))
        return min(self.ST[k][l],
                   self.ST[k][r - 2 ** k])


if __name__ == '__main__':
    a = list(map(int, input().split()))
    s = RMQSparseTable(a)
    while True:
        l, r = map(int, input().split())
        print(s.rmq(l, r))

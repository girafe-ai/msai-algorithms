class RSQFenwick:
    def __init__(self, N):
        self.N = N
        self.f = [0] * self.N

    def query(self, i):
        res = 0
        while i >= 0:
            res += self.f[i]
            i -= ~i & (i + 1)
        return res

    def update(self, i, delta):
        while i < self.N:
            self.f[i] += delta
            i += ~i & (i + 1)

    def rsq(self, left, right):
        return self.query(right - 1) - self.query(left - 1)


if __name__ == '__main__':
    N = int(input())
    s = RSQFenwick(N)
    while True:
        a, b, c = input().split()
        if a == '+':
            s.update(int(b), int(c))
        elif a == '?':
            print(s.rsq(int(b), int(c)))

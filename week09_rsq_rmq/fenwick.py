class RSQFenwick:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.f = [[0] * self.M for i in range(self.N)]

    def query(self, i, j):
        res = 0
        print('===')
        while i >= 0:
            while j >= 0:
                print(i, j)
                res += self.f[i][j]
                j -= ~j & (j + 1)
            i -= ~i & (i + 1)
        print('===')
        return res

    def update(self, i, j, delta):
        while i < self.N:
            while j < self.M:
                self.f[i][j] += delta
                j += ~j & (j + 1)
            i += ~i & (i + 1)

    def rsq(self, left, right):
        return self.query(right - 1) - self.query(left - 1)

from random import randint
if __name__ == '__main__':
    #a = list(map(int, input().split()))
    #N = int(input())
    s = RSQFenwick(100, 100)
    while True:
        s.query(randint(0, 99), randint(0, 99))


    while True:
        a, b, c = input().split()
        if a == '+':
            s.update(int(b), int(c))
        elif a == '?':
            print(s.rsq(int(b), int(c)))

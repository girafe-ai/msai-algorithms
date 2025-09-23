from math import sqrt, floor, ceil


class RSQSqrtDecomposition:
    def __init__(self, a):
        N = len(a)
        self.k = max(int(ceil(sqrt(N))), 1)
        self.a = a
        self.b = [0] * (self.k + 1)

        for i, v in enumerate(a):
            self.b[i // self.k] += v

    def rsq(self, l, r):
        l_block = self.k * int(ceil(l / self.k))
        r_block = self.k * int(floor(r / self.k))
        if l_block > r_block:
            return sum(self.a[l:r])
        return (sum(self.a[l:l_block]) +
                sum(self.b[l_block // self.k:r_block // self.k]) +
                sum(self.a[r_block:r]))

    def update(self, i, v):
        delta = v - self.a[i]
        self.a[i] = v
        self.b[i // self.k] += delta


if __name__ == '__main__':
    a = list(map(int, input().split()))
    s = RSQSqrtDecomposition(a)
    while True:
        a, b, c = input().split()
        if a == '+':
            s.update(int(b), int(c))
        elif a == '?':
            print(s.rsq(int(b), int(c)))
        elif a == '!':
            print(' '.join(map(str, s.a)))

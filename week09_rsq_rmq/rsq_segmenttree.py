from math import log2, floor, ceil


class RSQSegmentTree:
    neutral_value = 0

    def __init__(self, a):
        self.N = 2 ** int(ceil(log2(len(a))))
        self.s = [None] * (self.N - 1) + list(a) + ([self.neutral_value] * (self.N - len(a)))
        for i in range(self.N - 2, -1, -1):
            self.refresh_s(i)

    def refresh_s(self, i):
        self.s[i] = self.s[2 * i + 1] + self.s[2 * i + 2]

    def rsq_i(self, l, r, i, li, ri):
        if (r <= li) or (ri <= l):
            return self.neutral_value
        if (l <= li) and (ri <= r):
            return self.s[i]
        middle = li + (ri - li) // 2
        return (self.rsq_i(l, r, i * 2 + 1, li, middle) +
                self.rsq_i(l, r, i * 2 + 2, middle, ri))

    def update(self, i, v):
        i += self.N - 1
        self.s[i] = v
        while i > 0:
            i = (i - 1) // 2
            self.refresh_s(i)

    def rsq(self, l, r):
        return self.rsq_i(l, r, 0, 0, self.N)


if __name__ == '__main__':
    a = list(map(int, input().split()))
    #N = int(input())
    s = RSQSegmentTree(a)
    while True:
        a, b, c = input().split()
        if a == '+':
            s.update(int(b), int(c))
        elif a == '?':
            print(s.rsq(int(b), int(c)))
        elif a == '!':
            print(' '.join(map(str, s.a)))

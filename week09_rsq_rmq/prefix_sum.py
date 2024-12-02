class RSQPrefixSum:
    def __init__(self, a):
        self.s = [0]
        for v in a:
            self.s.append(self.s[-1] + v)

    def rsq(self, l, r):
        return self.s[r] - self.s[l]


if __name__ == '__main__':
    a = list(map(int, input().split()))
    s = RSQPrefixSum(a)
    while True:
        l, r = map(int, input().split())
        print(s.rsq(l, r))

def binsearch_exists(x, key):
    l = 0
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] <= key:
            l = m
        else:
            r = m
    return x[l] == key


def binsearch_left(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] < key:
            l = m
        else:
            r = m
    return r


def binsearch_right(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] <= key:
            l = m
        else:
            r = m
    return r


N = int(input())
x = list(map(int, input().split()))
x = sorted(x)
key = int(input())
print("YES" if binsearch_exists(x, key) else "NO")

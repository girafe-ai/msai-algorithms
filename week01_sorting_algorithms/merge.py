def merge(x, l, m, r):
    tmp = []
    i1 = l
    i2 = m
    while i1 < m or i2 < r:
        if (i2 >= r) or ((i1 < m) and
                         (x[i1] < x[i2])):
            tmp.append(x[i1])
            i1 += 1
        else:
            tmp.append(x[i2])
            i2 += 1
    x[l:r] = tmp


def merge_sort(x, l=0, r=None):
    if r is None:
        r = len(x)
    if r - l > 1:
        m = (l + r) // 2  # Finding the mid of the array
        merge_sort(x, l, m)  # Sorting the first half
        merge_sort(x, m, r)  # Sorting the second half
        merge(x, l, m, r)


input()
x = list(map(int, input().split()))
N = len(x)
merge_sort(x, 0, N)
print(' '.join(map(str, x)))
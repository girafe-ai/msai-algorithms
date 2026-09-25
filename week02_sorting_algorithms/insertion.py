def insertion_sort(x):
    N = len(x)
    for i in range(1, N):
        key = x[i]
        j = i - 1
        while j >= 0 and key < x[j]:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = key


if __name__ == '__main__':
    input()
    x = list(map(int, input().split()))
    print(' '.join(map(str, x)))

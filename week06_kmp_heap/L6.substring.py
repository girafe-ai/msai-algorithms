def find_substrings_naive(s, p):
    N = len(s)
    K = len(p)
    substrings = []
    for i in range(N - K + 1):
        if all([s[i + j] == p[j] for j in range(K)]):
            substrings.append(i)
    return substrings


def prefix_function(s):
    d = [0] * (len(s) + 1)
    for i in range(2, len(d)):
        d[i] = d[i - 1]
        while s[i - 1] != s[d[i]] and d[i] > 0:
            d[i] = d[d[i]]
        if s[i - 1] == s[d[i]]:
            d[i] += 1
    return d


def find_substrings_kmp(s, p):
    substrings = []
    d = prefix_function(p + '$' + s)
    for i in range(len(p) + 1, len(d)):
        if d[i] == len(p):
            substrings.append(i - 2 * len(p) - 1)
    return substrings


def find_substrings_native(s, p):
    i = -1
    substrings = []
    while True:
        i = s.find(p, i + 1)
        if i >= 0:
            substrings.append(i)
        else:
            return substrings


if __name__ == '__main__':
    s = input().strip()
    p = input().strip()



    print('Python: ', ' '.join(map(str, find_substrings_native(s, p))))
    print('Naive : ', ' '.join(map(str, find_substrings_naive(s, p))))
    print('KMP   : ', ' '.join(map(str, find_substrings_kmp(s, p))))

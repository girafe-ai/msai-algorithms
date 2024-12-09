from random import randint


def c_to_i(ch):
    return ord(ch) - ord('a') + 1


p = 10**9 + 7
a = randint(c_to_i('z') + 1, p - 1)


def find_substrings_rabin_karp(s, t):
    h = [0] * (len(s) + 1)
    a_pow = [1] * (len(s) + 1)
    for i in range(len(s)):
        h[i + 1] = (h[i] + c_to_i(s[i]) * a_pow[i]) % p
        a_pow[i + 1] = (a_pow[i] * a) % p

    h_t = 0
    for i in range(len(t)):
        h_t = (h_t + c_to_i(t[i]) * a_pow[i]) % p

    substrings = []
    for i in range(len(s) - len(t) + 1):
        if (h_t * a_pow[i]) % p == (h[i + len(t)] - h[i]) % p:
            if all([s[i + j] == t[j] for j in range(len(t))]):
                substrings.append(i)
    return substrings


if __name__ == '__main__':
    s = input().strip()
    t = input().strip()
    print(' '.join(map(str, find_substrings_rabin_karp(s, t))))

# Fixed parameters of quantum process:
quantum_a = 7**5
quantum_m = 2**31 - 1


def kth_smallest(x, k):
    x.sort()
    return x[k - 1]


def analyze_trimpazation(n, m, q0, k):
    m_div2 = m // 2
    q = q0
    # generating x data:
    x = []
    for i in range(n):
        x_i = q % m - m_div2
        x.append(x_i)
        q = ((q * quantum_a) % quantum_m)
    return kth_smallest(x, k)


if __name__ == '__main__':
    N, M, q0, k = map(int, input().split())
    print(analyze_trimpazation(N, M, q0, k))

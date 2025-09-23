if __name__ == '__main__':
    N = int(input())
    G = [{} for v in range(N)]
    E = []
    a = []
    for i in range(N):
        a.append(list(map(int, input().split())))

    d = [list(ai) for ai in a]
    for k in range(N):
        for v in range(N):
            for u in range(N):
                d[v][u] = min(d[v][u], d[v][k] + d[k][u])

    for di in d:
        print(' '.join(map(str, di)))

from heapq import heappush, heappop
inf = 10 ** 9


if __name__ == '__main__':
    N, M = map(int, input().split())
    G = [{} for i in range(N)]
    for i in range(M):
        x, y, weight = map(int, input().split())
        G[x][y] = weight
    s = int(input())

    h = []
    d = [inf] * N
    v = -1
    # added fictitious vertex to simplify
    # while with heappop:
    S = {-1}
    d[s] = 0
    heappush(h, (d[s], s))
    while h:
        while v in S and h:
            v = heappop(h)[1]
        if v not in S:
            S.add(v)
            for u in G[v]:
                new_d = d[v] + G[v][u]
                if new_d < d[u]:
                    heappush(h, (new_d, u))
                    d[u] = new_d

    print(' '.join(map(str, d)))

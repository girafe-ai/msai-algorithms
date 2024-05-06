from collections import deque
INF = 10**9

# with one color:
def bfs(G, s):
    visited = [False] * len(G)
    vertex_queue = deque([s])
    while vertex_queue:
        v = vertex_queue.popleft()
        if not visited[v]:
            visited[v] = True
            for u in G[v]:
                if not visited[u]:
                    vertex_queue.append(u)
    return visited


# with two colors for calculating path (+d, p):
def bfs_p(G, s):
    visited = [False] * len(G)
    d = [INF] * len(G)
    p = [-1] * len(G)
    d[s] = 0

    vertex_queue = deque([s])
    while vertex_queue:
        v = vertex_queue.popleft()
        visited[v] = 2
        for u in G[v]:
            if not visited[u]:
                visited[u] = 1
                vertex_queue.append(u)
                d[u] = d[v] + 1
                p[u] = v
    return d, p


if __name__ == '__main__':
    N, M = map(int, input().split())
    G = [[] for i in range(N)]

    for i in range(M):
        x, y = map(int, input().split())
        G[x].append(y)
        G[y].append(x)
    s, f = map(int, input().split())

    #searching shortest path s -> f:
    d, p = bfs_p(G, s)

    if d[f] == INF:
        print(-1)
    else:
        print(d[f])
        path = []
        i = f
        while i != s:
            path.append(i)
            i = p[i]
        path.append(s)
        print(' '.join(map(str, path[::-1])))

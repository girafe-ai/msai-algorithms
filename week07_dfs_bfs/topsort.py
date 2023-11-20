import sys


def dfs(G, visited, topsort, v):
    visited[v] = 1
    for u in G[v]:
        if not visited[u]:
            dfs(G, visited, topsort, u)
        elif visited[u] == 1:
            print('No')
            sys.exit(0)
    visited[v] = 2
    topsort.append(v)


def dfs_nonrec(G, visited, topsort, s):
    vertex_stack = [s]
    while vertex_stack:
        v = vertex_stack[-1]
        if not visited[v]:
            visited[v] = 1
            for u in G[v]:
                if not visited[u]:
                    vertex_stack.append(u)
                elif visited[u] == 1:
                    print('No')
                    sys.exit(0)
        else:
            # all neighbours of v were visited
            if visited[v] == 1:
                topsort.append(v)
            visited[v] = 2
            vertex_stack.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    G = [[] for i in range(N)]

    for i in range(M):
        x, y = map(int, input().split())
        G[x].append(y)

    visited = [False] * len(G)

    topsort = []
    for i in range(N):
        if not visited[i]:
            dfs_nonrec(G, visited, topsort, i)

    topsort = [v for v in topsort]

    print('Yes')
    print(' '.join(map(str, topsort[::-1])))

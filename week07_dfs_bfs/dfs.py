from itertools import groupby
#import sys
#sys.setrecursionlimit(640000000)


# just traverses all vertices reachable from v:
def dfs(G, visited, v):
    visited[v] = True
    for n in G[v]:
        if not visited[n]:
            dfs(G, visited, n)


# just traverses all vertices reachable from v:
def dfs_nonrec_1(G, visited, s):
    vertex_stack = [s]
    while vertex_stack:
        v = vertex_stack.pop()
        if not visited[v]:
            visited[v] = True
            for u in G[v]:
                if not visited[u]:
                    vertex_stack.append(u)


# allows to get a moment when we color vertex with blue:
# (like ending of executing dfs(v) for recursive case)
def dfs_nonrec_2(G, visited, s):
    vertex_stack = [s]
    while vertex_stack:
        v = vertex_stack[-1]
        if not visited[v]:
            visited[v] = True
            for u in G[v]:
                if not visited[u]:
                    vertex_stack.append(u)
        else:
            # all neighbours of v were visited
            vertex_stack.pop()


# checks for cycles in undirected graph:
def dfs_cycles_undirected(G, visited, v, p=-1):
    visited[v] = True
    for u in G[v]:
        if not visited[u]:
            dfs_cycles_undirected(G, visited, u, v)
        else:
            if u != p:
                print('Cycle found!')


def dfs_cycles_undirected_nonrec(G, visited, s):
    vertex_stack = [(s, -1)]
    while vertex_stack:
        v, p = vertex_stack[-1]
        if not visited[v]:
            visited[v] = True
            for u in G[v]:
                if not visited[u]:
                    vertex_stack.append((u, v))
                else:
                    if u != p:
                        print('Cycle found!')
        else:
            # all neighbours of v were visited
            vertex_stack.pop()


# checks for cycles in directed graph:
def dfs_cycles_directed(G, visited, v):
    visited[v] = 1
    for u in G[v]:
        if not visited[u]:
            dfs(G, visited, u)
        elif visited[u] == 1:
            print('Cycle found!')
    visited[v] = 2


def dfs_cycles_directed_nonrec(G, visited, s):
    vertex_stack = [s]
    while vertex_stack:
        v = vertex_stack[-1]
        if not visited[v]:
            visited[v] = 1
            for u in G[v]:
                if not visited[u]:
                    vertex_stack.append(u)
                elif visited[u] == 1:
                    print('Cycle found!')
        else:
            # all neighbours of v were visited
            visited[v] = 2
            vertex_stack.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    G = [[] for i in range(N)]

    for i in range(M):
        x, y = map(int, input().split())
        G[x].append(y)
        G[y].append(x)

    # calculating number of connected components:

    visited = [False] * len(G)
    n_components = 0
    for i in range(N):
        if not visited[i]:
            n_components += 1
            dfs(G, visited, i)

    print(n_components)

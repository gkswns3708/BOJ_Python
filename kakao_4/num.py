import sys
from collections import deque


def possible_st(adj, n, paths, gates, summits, intensity):
    que = deque()
    visited = [False for _ in range(n + 1)]
    goal = []

    for gate in gates:
        visited[gate] = True
        que.append((gate, gate))
    for summit in summits:
        visited[summit] = None

    while que:
        n_pos, st_pos = que.popleft()

        for nxt_pos, weight in adj[n_pos]:
            if weight <= intensity:
                if visited[nxt_pos] == None:
                    visited[nxt_pos] = True
                    goal.append(nxt_pos)
                elif visited[nxt_pos] == True:
                    continue
                elif visited[nxt_pos] == False:
                    visited[nxt_pos] = True
                    que.append((nxt_pos, st_pos))
    return goal


def solution(n, paths, gates, summits):
    lo, hi = 0, 10000000
    adj = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        adj[i].append((j, w))
        adj[j].append((i, w))
    while lo + 1 < hi:
        mid = (lo + hi) // 2  # mid 이상은 intensity 가능
        possible = possible_st(adj, n, paths, gates, summits, mid)
        if possible:
            ans = possible
            hi = mid
        else:
            lo = mid
    return [min(ans), hi]


n = 7
paths = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
gates = [1]
summits = [2, 3, 4]

print(solution(n, paths, gates, summits))

import sys
from collections import deque

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

n, m = None, None
adj = None
dist = None
parents = None


def set_variable():
    global n, m, adj, dist, parents
    n, m = get_line()
    dist = [-sys.maxsize for _ in range(n + 1)]
    adj = [[] for _ in range(n + 1)]
    parents = [0 for x in range(n + 1)]
    for _ in range(m):
        u, v, m = get_line()
        adj[u].append((v, m))


def solution():
    global n, m, adj, dist, parents
    dist[1] = 0
    for i in range(n):
        for j in range(1, n + 1):
            for nxt, cost in adj[j]:
                if dist[nxt] < dist[j] + cost and dist[j] != -sys.maxsize:
                    dist[nxt] = dist[j] + cost
                    parents[nxt] = j
                    if i == n - 1 and dist[j] != -sys.maxsize:
                        dist[nxt] = sys.maxsize

    # tracking
    if dist[n] == sys.maxsize:
        print(-1)
    else:
        answer = []
        pos = n
        while pos != 0:
            answer.append(pos)
            pos = parents[pos]
        print(*answer[::-1])


if __name__ == "__main__":
    set_variable()
    solution()

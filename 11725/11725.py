import sys
from collections import deque

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N = None
adj = None
parents = None
visited = None


def set_variable():
    global N, adj, parents, visited
    N = get_input()
    adj = [[] for _ in range(N + 1)]
    parents = [None for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = get_line()
        adj[a].append(b)
        adj[b].append(a)


def solution():
    global N, adj, parents

    def BFS():
        que = deque()
        que.append(1)  # root node
        visited[1] = True

        while que:
            now_parents = que.popleft()
            for child in adj[now_parents]:
                if visited[child] == False:
                    parents[child] = now_parents
                    que.append(child)
                    visited[child] = True

    BFS()
    for i in range(2, N + 1):
        print(parents[i])


if __name__ == "__main__":
    set_variable()
    solution()

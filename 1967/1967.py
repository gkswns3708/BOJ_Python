import sys
from collections import deque

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())


V = None
adj = None
visited = None
dist = None


def set_variable():
    global V, adj, visited, dist
    V = get_input()
    adj = [[] for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)]
    dist = [sys.maxsize for _ in range(V + 1)]
    for _ in range(V - 1):
        u, v, w = get_line()
        adj[u].append((v, w))
        adj[v].append((u, w))


def solution():
    global V, adj, visited

    def BFS(st_idx):
        # init variable
        global V, adj, visited
        visited = [False for _ in range(V + 1)]
        dist = [sys.maxsize for _ in range(V + 1)]

        que = deque()
        que.append((st_idx, 0))
        visited[st_idx] = True
        dist[st_idx] = 0

        while que:
            now_pos, now_dist = que.popleft()

            for nxt_pos, weight in adj[now_pos]:
                if visited[nxt_pos] == False:
                    visited[nxt_pos] = True
                    que.append((nxt_pos, now_dist + weight))
                    dist[nxt_pos] = now_dist + weight
        return dist

    temp = BFS(1)
    temp_V = temp.index(max(temp[1:]))

    temp = BFS(temp_V)
    ans = max(temp[1:])
    print(ans)


if __name__ == "__main__":
    set_variable()
    solution()

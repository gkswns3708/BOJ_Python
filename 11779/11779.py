import sys
import heapq

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N, M = None, None
st, ed = None, None
adj = None
dist = None
visited = None
parents = None


def set_variable():
    global N, M, st, ed, adj, visited, dist, parents
    N = get_input()
    M = get_input()
    visited = [False for _ in range(N + 1)]
    dist = [sys.maxsize for _ in range(N + 1)]
    parents = [-1 for _ in range(N + 1)]
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        f, t, l = get_line()
        adj[f].append((t, l))
    st, ed = get_line()


def solution():
    global N, M, st, ed, adj, visited, dist, parents

    def Dijkstra():
        heap = []
        heapq.heappush(heap, (0, st))
        visited[st] = True
        dist[st] = 0
        parents[st] = -2

        while heap:
            n_dist, now = heapq.heappop(heap)

            if now == ed:
                back_trace = [ed]
                pos = ed
                while parents[pos] != -2:
                    back_trace.append(parents[pos])
                    pos = parents[pos]
                return n_dist, len(back_trace), back_trace

            for nxt, weight in adj[now]:
                if dist[nxt] > n_dist + weight:
                    dist[nxt] = n_dist + weight
                    parents[nxt] = now
                    heapq.heappush(heap, (n_dist + weight, nxt))

    ans_dist, ans_len, ans_list = Dijkstra()
    print(ans_dist)
    print(ans_len)
    print(*ans_list[::-1])


if __name__ == "__main__":
    set_variable()
    solution()

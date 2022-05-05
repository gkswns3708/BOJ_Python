import sys
import heapq

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

heap = []
V, E = get_line()
st_idx = get_input()
dist = [sys.maxsize] * (V + 1)
adj = [[] for i in range(V + 1)]


def Dijkstra(st_idx):
    dist[st_idx] = 0
    heapq.heappush(heap, (0, st_idx))

    while heap:
        ndist, npos = heapq.heappop(heap)

        if dist[npos] < ndist:
            continue

        for nxt_pos, weight in adj[npos]:
            nxt_dist = ndist + weight

            if nxt_dist < dist[nxt_pos]:
                dist[nxt_pos] = nxt_dist
                heapq.heappush(heap, (nxt_dist, nxt_pos))


for i in range(E):
    u, v, w = get_line()
    adj[u].append((v, w))

Dijkstra(st_idx)


for i in range(1, V + 1):
    print("INF" if dist[i] == sys.maxsize else dist[i])

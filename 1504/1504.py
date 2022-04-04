import sys
import heapq
get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

def Dijkstra(st_idx, dist, heap):
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

if __name__ == '__main__':
    # Input & Define
    N, E = get_line()
    adj = [[] for i in range(N + 1)]
    dist_v1 = [sys.maxsize] * (N + 1)
    dist_v2 = [sys.maxsize] * (N + 1)
    heap = []

    for i in range(E):
        a, b, c = get_line()
        adj[a].append((b,c))
        adj[b].append((a,c))

    v1, v2 = get_line()
    Dijkstra(v1, dist_v1, heap)
    Dijkstra(v2, dist_v2, heap)
    # 1 -> v1 -> v2 -> N, 1 -> v2 -> v1 -> N 이렇게 시나리오가 2개
    answer = min(dist_v1[1] + dist_v2[N], dist_v1[N] + dist_v2[1])
    answer += dist_v1[v2]

    if answer >= sys.maxsize :
        print(-1)
    else:
        print(answer)
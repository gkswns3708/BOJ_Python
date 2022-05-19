import sys
import heapq

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

def Dijkstra(N, M, A, B, C, mid):
    dist = [sys.maxsize for _ in range(N + 1)]
    heap = []
    heapq.heappush(heap, (0, A))
    dist[A] = 0
    while heap:
        now_dist, now_pos = heapq.heappop(heap)
        if now_dist > dist[now_pos]:
            continue
        
        if now_pos == B and dist[B] <= C:
            return True

        for nxt_pos, weight in adj[now_pos]:
            if dist[nxt_pos] > (now_dist + weight) and weight <= mid:
                dist[nxt_pos] = now_dist + weight
                heapq.heappush(heap, (dist[nxt_pos], nxt_pos))

    return False


if __name__ == "__main__":
    N, M, A, B, C = get_line()
    adj = [[] for _ in range(N + 1)]
    max_price = 0
    for _ in range(M):
        st, ed, cost = get_line()
        adj[st].append((ed, cost))
        adj[ed].append((st, cost))
        max_price = max(max_price, cost)

    l, r = 0, max_price + 1
    ans = None
    while l + 1 < r:
        mid = (l + r) // 2
        if Dijkstra(N, M, A, B, C, mid):
            ans = mid
            r = mid
        else:
            l = mid
    if ans != None:
        print(ans)
    else:
        print(-1)

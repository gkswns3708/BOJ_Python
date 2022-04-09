import sys
import heapq

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

V, E = None, None
dist, adj = None, None
heap = None


def set_variable():
    global V, E, adj, heap, dist
    V, E = get_line()
    adj = [[] for _ in range(V + 1)]
    dist = [[sys.maxsize for _ in range(V + 1)] for _ in range(V + 1)]
    heap = []
    for _ in range(E):
        a, b, c = get_line()
        adj[a].append((b, c))
        dist[a][b] = c
        heapq.heappush(heap, (c, a, b))


def solution():
    global V, E, adj, heap, dist

    def Dijkstra():
        while heap:
            c, a, b = heapq.heappop(heap)
            if a == b:
                return c
            else:
                for nxt_pos, weight in adj[b]:
                    if c + weight < dist[a][nxt_pos]:
                        dist[a][nxt_pos] = c + weight
                        heapq.heappush(heap, (c + weight, a, nxt_pos))
        return -1

    print(Dijkstra())


if __name__ == "__main__":
    set_variable()
    solution()

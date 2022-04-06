import sys
import heapq

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

n, m, t = None, None, None
s, g, h = None, None, None
adj = None
x_list = None
heap = None
ans_list = None


def set_variable():
    global n,m,t,s,g,h, adj, x_list,heap, ans_list
    def init_variable():
        global n,m,t,s,g,h, adj, x_list,heap, ans_list
        n, m, t = None, None, None
        s, g, h = None, None, None
        x_list = []
        heap = []
        ans_list = []

    init_variable()
    n, m, t = get_line()
    s, g, h = get_line()
    adj = [[] for i in range(n + 1)]
    dist = [sys.maxsize] * (n + 1)
    for _ in range(m):
        a, b, d = get_line()
        adj[a].append((b, d))
        adj[b].append((a, d))
    for _ in range(t):
        x = get_input()
        x_list.append(x)


def solution():
    global n,m,t,s,g,h, dist_s, dist_h, dist_g, adj, x_list,heap, ans_list
    def Dijkstra(dist, st_idx):
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
        return dist

    dist_s = Dijkstra(dist_s, s)
    dist_g = Dijkstra(dist_g, g)
    dist_h = Dijkstra(dist_h, h)

    for x in x_list:
        s_to_x = dist_s[x]
        s_to_g = dist_s[g]
        s_to_h = dist_s[h]
        g_to_x = dist_g[x]
        g_to_h = dist_g[h]
        h_to_x = dist_h[x]
        h_to_g = dist_h[g]

        if s_to_x == s_to_g + g_to_h + h_to_x or s_to_x == s_to_h + h_to_g + g_to_x:
            ans_list.append(x)
    print(*sorted(ans_list))


if __name__ == "__main__":
    TC = get_input()
    for _ in range(TC):
        set_variable()
        solution()

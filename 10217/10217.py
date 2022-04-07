import sys
import heapq

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N, M, K = None, None, None
dist_dp = None
heap, adj = None, None

def set_variable():
    global N, M, K, dist_dp, adj, heap
    N, M, K = get_line()
    dist_dp = [[sys.maxsize for _ in range(10000+1)] for _ in range(100 + 1)]  
    adj = [[] for _ in range(N + 1)]
    heap = []
    for _ in range(K):
        u, v, c, d = get_line()
        adj[u].append((v,c,d)) # nxt_pos, cost, dist_dp



def solution():
    global N, M, K, dist_dp, adj, heap
    def Dijkstra():
        dist_dp[1][0] = 0
        heapq.heappush(heap, (0, 1, 0)) # now_dist, now_pos, now_money
        while heap:
            sum_, nowpos, nowcost = heapq.heappop(heap)
            if dist_dp[nowpos][nowcost] < sum_:
                continue
            for nextpos, nxtweight, time in adj[nowpos]:
                if nowcost + nxtweight <= M:
                    if dist_dp[nextpos][nowcost + nxtweight] > dist_dp[nowpos][nowcost] + time:
                        dist_dp[nextpos][nowcost + nxtweight] = dist_dp[nowpos][nowcost] + time
                        heapq.heappush(heap, (dist_dp[nextpos][nowcost + nxtweight], nextpos, nowcost + nxtweight))
    Dijkstra()
    ans = min(dist_dp[N][:M])
    if ans == sys.maxsize:
        print("Poor KCM")
    else:
        print(ans)

    
if __name__ == "__main__":
    TC = get_input()
    for _ in range(TC):
        set_variable()
        solution()
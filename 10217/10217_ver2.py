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
    dist_dp = [[sys.maxsize for _ in range(M + 1)] for _ in range(N + 1)]
    adj = [[] for _ in range(N + 1)]
    heap = []
    for _ in range(K):
        u, v, c, d = get_line()
        adj[u].append((v, c, d))  # nxt_pos, cost, dist_dp


def solution():
    global N, M, K, dist_dp, adj, heap

    def Dijkstra():
        dist_dp[1][0] = 0
        for c in range(M + 1):
            for d in range(1, N + 1):
                if dist_dp[d][c] == sys.maxsize:
                    continue
                t = dist_dp[d][c]
                for nv, nc, nd in adj[d]:
                    if c + nc <= M:
                        dist_dp[nv][c + nc] = min(
                            dist_dp[nv][c + nc], dist_dp[d][c] + nd
                        )

    Dijkstra()
    ans = min(dist_dp[N])
    if ans == sys.maxsize:
        print("Poor KCM")
    else:
        print(ans)


if __name__ == "__main__":
    TC = get_input()
    for _ in range(TC):
        set_variable()
        solution()

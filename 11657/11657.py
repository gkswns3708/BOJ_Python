import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())


N, M = None, None
adj = None
dist = None


# Time complexity O(NM)
def bellman_ford():
    dist[1] = 0
    check = True
    for i in range(N):
        for now_pos in range(1, N + 1):
            for nxt_pos, weight in adj[now_pos]:
                if (
                    dist[now_pos] != sys.maxsize
                    and dist[nxt_pos] > dist[now_pos] + weight
                ):
                    dist[nxt_pos] = dist[now_pos] + weight
                    if i == N - 1:
                        check = False

    return dist, check


def set_variable():
    global N, M, adj, dist

    def init_variable():
        N, M, adj, dist = None, None, None, None

    init_variable()
    N, M = get_line()
    adj = [[] for _ in range(N + 1)]
    dist = [sys.maxsize] * (N + 1)
    for _ in range(M):
        a, b, c = get_line()
        adj[a].append((b, c))


def solution():
    ans_dist, check = bellman_ford()
    if check:
        for ans in ans_dist[2:]:
            if ans == sys.maxsize:
                print(-1)
            else:
                print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    set_variable()
    solution()

import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

n, m, adj = None, None, None


def set_variable():
    global n, m, adj
    n = get_input()
    m = get_input()
    adj = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = get_line()
        adj[a][b] = min(adj[a][b], c)

    for i in range(1, n + 1):
        adj[i][i] = 0


def solution():
    global n, m, adj

    def floyd_warshall():
        for m in range(1, n + 1):
            for s in range(1, n + 1):
                for e in range(1, n + 1):
                    if adj[s][m] != sys.maxsize and adj[m][e] != sys.maxsize:
                        adj[s][e] = min(adj[s][e], adj[s][m] + adj[m][e])

    floyd_warshall()
    for i in range(1, n + 1):
        ans_list = []
        for j in range(1, n + 1):
            if adj[i][j] == sys.maxsize:
                ans_list.append(0)
            else:
                ans_list.append(adj[i][j])
        print(*ans_list)

if __name__ == "__main__":
    set_variable()
    solution()

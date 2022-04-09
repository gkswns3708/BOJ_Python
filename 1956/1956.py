import sys
get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

V, E = None, None
adj = None

def set_variable():
    global V, E, adj
    V, E = get_line()
    adj = [[sys.maxsize for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(E):
        a, b, c = get_line()
        adj[a][b] = c
    for i in range(1, V + 1):
        adj[i][i] = 0

def solution():
    global V, E, adj
    def floyd_warshall():
        for m in range(1, V + 1):
            for s in range(1, V + 1):
                for e in range(1, V + 1):
                    if adj[s][m] != sys.maxsize and adj[m][e] != sys.maxsize:
                        adj[s][e] = min(adj[s][e], adj[s][m] + adj[m][e])

    floyd_warshall()
    ans = sys.maxsize
    for i in range(1, V + 1):
        for j in range(i + 1, V + 1):
            if adj[i][j] == sys.maxsize or adj[j][i] == sys.maxsize:
                continue
            ans = min(ans, adj[i][j] + adj[j][i])
    
    if ans == sys.maxsize:
        print(-1)
    else:
        print(ans)
    
                            
    

if __name__ == "__main__":
    set_variable()
    solution()

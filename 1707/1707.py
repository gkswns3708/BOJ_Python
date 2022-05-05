import sys
from collections import deque

sys.setrecursionlimit(int(1e8))
get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

V, E = None, None
adj = None
color_arr = None
visited = None


def set_variable():
    global V, E, adj, visited, color_arr
    V, E = get_line()
    adj = [[] for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)]
    color_arr = [None for _ in range(V + 1)]
    for _ in range(E):
        st, ed = get_line()
        adj[st].append(ed)
        adj[ed].append(st)


def BFS_solution():
    global V, E, adj, visited, color_arr

    def BFS(st):
        que = deque()
        que.append(st)
        color = 0
        color_arr[st] = color
        while que:
            sz = len(que)
            for _ in range(sz):
                now = que.popleft()
                for nxt in adj[now]:
                    if color_arr[nxt] == None:
                        color_arr[nxt] = (color + 1) % 2
                        que.append(nxt)
                    elif color_arr[nxt] == color:
                        return False
                    elif color_arr[nxt] != color:
                        continue
            color = (color + 1) % 2
        return True

    for i in range(1, V + 1):
        if color_arr[i] == None:
            check = BFS(i)
            if check == False:
                print("NO")
                return
    print("YES")
    return


if __name__ == "__main__":
    TC = get_input()
    for _ in range(TC):
        set_variable()
        BFS_solution()
        # DFS_solution()

import sys
from collections import deque

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N, M, H = None, None, None
arr = None
visited = None


def possible(z, y, x):
    global N, M, H, arr, visited
    if (x >= 0) and (x < N) and (y >=0) and (y < M) and (z >= 0) and (z < H) and (arr[z][y][x] == 0) and (visited[z][y][x] == False):
        return True
    else:
        return False

def set_variable():
    global N, M, H, arr, visited
    N, M, H = get_line()
    arr = [[[None for _ in range(N + 1)] for _ in range(M  + 1)] for _ in range(H + 1)]
    visited = [[[False for _ in range(N + 1)] for _ in range(M + 1)] for _ in range(H + 1)]
    for z in range(H):
        for y in range(M):
            tmp = list(get_line())
            for x, value in enumerate(tmp):
                arr[z][y][x] = value

def solution():
    global N, M, H, arr, visited
    deq = deque()
    day = 0
    check = True
    for z in range(H):
        for y in range(M):
            for x in range(N):
                if arr[z][y][x] == 1:
                    visited[z][y][x] = True
                    deq.appendleft((z, y, x))

    dx = [0, 0, 0, 0, 1, -1]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [-1, 1, 0, 0, 0, 0]
    
    while deq:
        cnt = len(deq)
        for idx in range(cnt):
            z, y, x = deq.popleft()
            for i in range(6):
                nxt_z = z + dz[i]
                nxt_y = y + dy[i]
                nxt_x = x + dx[i]

                if possible(nxt_z, nxt_y, nxt_x):
                    visited[nxt_z][nxt_y][nxt_x] = True
                    deq.append((nxt_z, nxt_y, nxt_x))
        day += 1
    
    for z in range(H):
        for y in range(M):
            for x in range(N):
                if visited[z][y][x] == False and arr[z][y][x] == 0:
                    check = False
    
    if check:
        print(day - 1)
    else:
        print(-1)

if __name__ == "__main__":
    set_variable()
    solution()

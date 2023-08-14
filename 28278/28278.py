import sys
from collections import deque

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N = get_input()
que = deque()

for _ in range(N):
    now_input = list(get_line())
    if now_input[0] == 1:
        que.append(now_input[1])
    elif now_input[0] == 2:
        if que:
            print(que.pop())
        else:
            print(-1)
    elif now_input[0] == 3:
        print(len(que))        
    elif now_input[0] == 4:
        if que:
            print(0)
        else:
            print(1)
    else:
        if que:
            print(que[-1])
        else:
            print(-1)
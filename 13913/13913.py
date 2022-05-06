import sys
from collections import deque

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N, K = None, None
parents = None


def set_variable():
    global N, K, parents
    N, K = get_line()
    parents = [-1 for _ in range(200000 + 1)]


def solution():
    global N, K, parents

    def possible(pos):
        if pos >= 0 and pos <= 200000 and parents[pos] == -1:
            return True
        else:
            return False

    def trace_back():
        pos = K
        ans_list = [K]
        while parents[pos] != -2:
            ans_list.append(parents[pos])
            pos = parents[pos]
        return ans_list[::-1]

    que = deque()
    que.append(N)
    parents[N] = -2

    while que:
        now = que.popleft()

        for nxt in [now + 1, now - 1, now * 2]:
            if possible(nxt):
                que.append(nxt)
                parents[nxt] = now
    ans_list = trace_back()
    print(len(ans_list) - 1)
    print(*ans_list)


if __name__ == "__main__":
    set_variable()
    solution() 

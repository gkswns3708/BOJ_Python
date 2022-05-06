import sys
from collections import deque

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())


def solution():
    A, B = get_line()
    visited = [False for _ in range(10000)]
    parents = [None for _ in range(10000)]

    def possible(pos):
        if visited[pos] == False:
            return True
        else:
            return False

    def trace_back():
        ans_string = ""
        pos = B
        while parents[pos] != None:
            nxt, oper = parents[pos]
            ans_string += oper
            pos = nxt

        return ans_string[::-1]

    que = deque()
    que.append(A)
    visited[A] = True
    parents[A] = None
    while True:
        now = que.popleft()
        if now == B:
            print(trace_back())
            return
        else:
            for i in "DSLR":
                child = now
                if i == "D":
                    nxt = (child * 2) % 10000
                elif i == "S":
                    nxt = (child + 9999) % 10000
                elif i == "L":
                    nxt = child % 1000 * 10 + child // 1000
                elif i == "R":
                    nxt = child % 10 * 1000 + child // 10
                if possible(nxt):
                    visited[nxt] = True
                    parents[nxt] = (now, i)
                    que.append(nxt)


if __name__ == "__main__":
    TC = get_input()
    for _ in range(TC):
        solution()

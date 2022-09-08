import sys
from pprint import pprint

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N, X = None, None


def set_variable():
    global N, X
    X = get_input()
    N = get_input()


def solution():
    global N, X
    for _ in range(N):
        price, n = get_line()
        X -= price * n

    if X == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    set_variable()
    solution()

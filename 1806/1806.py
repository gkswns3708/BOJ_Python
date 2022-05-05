from re import S
import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N, S = None, None
arr = None


def set_variable():
    global N, S, arr
    N, S = get_line()
    arr = list(get_line())


def solution():
    global N, S, arr
    l, r, sum, min_length = 0, 0, arr[0], sys.maxsize
    while r < len(arr):
        if sum >= S:
            min_length = min(min_length, r - l + 1)
            sum -= arr[l]
            l += 1
        else:
            r += 1
            if r >= len(arr):
                break
            sum += arr[r]
    if min_length == sys.maxsize:
        print(0)
    else:
        print(min_length)


if __name__ == "__main__":
    set_variable()
    solution()

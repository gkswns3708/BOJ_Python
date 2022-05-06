import sys
from pprint import pprint

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

s1, s2 = None, None
N, M = None, None
arr = None
char_arr = None


def set_variable():
    global s1, s2, arr, char_arr
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()
    N, M = len(s1), len(s2)
    arr = [["" for _ in range(M + 1)] for _ in range(N + 1)]


def solution():
    global s1, s2, arr, char_arr
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + s1[i - 1]
            else:
                if len(arr[i - 1][j]) >= len(arr[i][j - 1]):
                    arr[i][j] = arr[i - 1][j]
                else:
                    arr[i][j] = arr[i][j - 1]
    if arr[-1][-1] == "":
        print(0)
    else:
        print(len(arr[-1][-1]))
        print(arr[-1][-1])


if __name__ == "__main__":
    set_variable()
    solution()

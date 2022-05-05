import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N = None
deq = None


def main():
    global N, deq
    N = get_input()
    input_arr = list(get_line())
    stack = []
    out = [-1 for _ in range(N)]
    for idx, now_num in enumerate(input_arr):
        while stack and stack[-1][0] < now_num:
            out[stack.pop(-1)[1]] = now_num
        stack.append((now_num, idx))
    print(*out)


if __name__ == "__main__":
    main()

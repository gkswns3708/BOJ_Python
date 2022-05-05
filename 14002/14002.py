import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N = None
arr = None
dp = None


def set_variable():
    global N, arr, dp
    N = get_input()
    arr = list(get_line())
    dp = [1 for _ in range(N + 1)]


def solution():
    global N, arr, dp
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))

    max_dp = max(dp)
    ans_list = []
    for i in range(N - 1, -1, -1):
        if dp[i] == max_dp:
            ans_list.append(arr[i])
            max_dp -= 1

    print(*ans_list[::-1])


if __name__ == "__main__":
    set_variable()
    solution()

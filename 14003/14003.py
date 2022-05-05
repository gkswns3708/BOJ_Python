import sys
import bisect

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N = None
arr = None
dp_table = None
cnt = None


def set_variable():
    global N, arr, dp_table, cnt
    N = get_input()
    arr = list(get_line())
    dp_table = [arr[0]]
    cnt = [0 for _ in range(N)]
    cnt[0] = 1


def solution():
    global N, arr, dp_table, cnt
    for i in range(1, N):
        if dp_table[-1] < arr[i]:
            dp_table.append(arr[i])
            cnt[i] = len(dp_table)
        else:
            idx = bisect.bisect_left(dp_table, arr[i])
            dp_table[idx] = arr[i]
            cnt[i] = idx + 1

    max_dp = len(dp_table)
    ans = []
    for i in range(N - 1, -1, -1):
        if cnt[i] == max_dp:
            ans.append(arr[i])
            max_dp -= 1

    print(len(ans))
    print(*ans[::-1])


if __name__ == "__main__":
    set_variable()
    solution()

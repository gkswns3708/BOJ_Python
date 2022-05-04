import sys
sys.setrecursionlimit(int(1e8))
get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())


N = None
dp_table = None
arr = None

def set_variable():
    global N, dp_table, arr
    N = get_input()
    arr = []
    dp_table = [[-1 for _ in range(N)] for _ in range(N)]
    for _ in range(N):
        r, c = get_line()
        arr.append([r,c])
    

def solution(s, e):
    if s == e:
        return 0
    elif dp_table[s][e] != -1:
        return dp_table[s][e]
    elif s + 1 == e:
        dp_table[s][e] = arr[s][0] * arr[s][1] * arr[e][1]
        return dp_table[s][e]
    else:
        for i in range(s, e):
            ret = solution(s, i) + solution(i + 1, e) + (arr[s][0] * arr[i][1] *arr[e][1])
            if dp_table[s][e] == -1 or dp_table[s][e] > ret:
                dp_table[s][e] = ret
    return dp_table[s][e]

if __name__ == "__main__":
    set_variable()
    print(solution(0, N - 1))

import sys
from pprint import pprint

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

S = None
N = None
cnt = None


def main():
    global S, N, cnt

    def solution(cnt, a, S, l, r):
        return cnt[ord(a) - 97][r] - cnt[ord(a) - 97][l] + int(S[l] == a)

    def make_cnt(S):
        cnt_arr = []
        for alphabet in "abcdefghijklmnopqrstuvwxyz":
            temp = [0 for _ in S]
            cnt = 0
            for idx, S_alphabet in enumerate(S):
                if idx == 0:
                    temp[idx] = int(S_alphabet == alphabet)
                else:
                    temp[idx] = temp[idx - 1] + int(S_alphabet == alphabet)
            cnt_arr.append(temp)
        return cnt_arr

    S = sys.stdin.readline().rstrip()
    N = get_input()
    cnt = make_cnt(S)
    for _ in range(N):
        a, l, r = sys.stdin.readline().rstrip().split()
        l, r = int(l), int(r)
        sys.stdout.write(str(solution(cnt, a, S, l, r)) + "\n")


if __name__ == "__main__":
    main()

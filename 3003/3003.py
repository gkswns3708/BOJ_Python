# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
import sys

get_line = lambda : map(int, sys.stdin.readline().rstrip().split())
get_input = lambda : int(sys.stdin.readline().strip())

chess_list = get_line()
for chess_cnt, cnt in zip(chess_list, [1, 1, 2, 2, 2, 8]):
    print(cnt - chess_cnt, end=" ")
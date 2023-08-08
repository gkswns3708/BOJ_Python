import sys
from collections import defaultdict

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N, M = None, None
cnt_dict = None

def set_variable():
    global N, M, cnt_dict
    N, M = get_line() # N, M 입력 받음
    cnt_dict = defaultdict(int)
    for _ in range(N):
        vocab = sys.stdin.readline().strip()
        if len(vocab) < M:
            continue
        else:
            cnt_dict[vocab] += 1
    

def solution():
    global N, M, cnt_dict
    answer = sorted(cnt_dict.items(), key=lambda x : (-x[1],  -len(x[0]), x[0]))
    answer = [i[0] for i in answer]
    print('\n'.join(answer)) 


if __name__ == "__main__":
    set_variable()
    solution()
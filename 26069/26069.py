import sys
from collections import defaultdict

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N = None
arr_set = None

def set_variable():
    global N, arr_set
    N = get_input()
    arr_set = defaultdict(int)
    arr_set["ChongChong"] = 1
    for _ in range(N):
        name1, name2 = sys.stdin.readline().rstrip().split()
        arr_set[name1] = max(arr_set[name1], arr_set[name2])
        arr_set[name2] = max(arr_set[name1], arr_set[name2])
    
    print(sum(arr_set.values()))

if __name__ == "__main__":
    set_variable()
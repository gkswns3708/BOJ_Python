import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N, K = None, None
input_list = None

def set_variable():
    global N, K, input_list
    N, K = get_line()
    input_list = list(get_line())


def solution():
    global N, K, input_list
    print(sorted(input_list,reverse=True)[K])

if __name__ == "__main__":
    set_variable()
    solution()

import sys

sys.setrecursionlimit(10 ** 5)
get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

adj = None
pre_order = None
N = None


def set_variable():
    global adj, pre_order, N
    pre_order = []
    while True:
        try:
            pre_order.append(get_input())
        except:
            break
    N = len(pre_order)


def solution():
    global adj, pre_order, N

    def print_post_order(st, ed):
        if st > ed:
            return
        root = pre_order[st]
        search_idx = st + 1
        while search_idx <= ed:
            if pre_order[search_idx] > root:
                break
            search_idx += 1
        print_post_order(st + 1, search_idx - 1)
        print_post_order(search_idx, ed)

        print(root)

    print_post_order(0, N - 1)


if __name__ == "__main__":
    set_variable()
    solution()

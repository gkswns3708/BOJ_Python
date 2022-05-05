import sys

sys.setrecursionlimit(10**8)
get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())


def main():
    def set_variable():
        def find_parents(a, parents):
            if a == parents[a]:
                return a
            else:
                parents[a] = find_parents(parents[a], parents)
                return parents[a]

        def _union(a, b, parents):
            a = find_parents(a, parents)
            b = find_parents(b, parents)
            parents[b] = a

        def _check(a, b, parents):
            a = find_parents(a, parents)
            b = find_parents(b, parents)
            return a == b

        N, M = get_line()
        parents = [i for i in range(N + 1)]
        for _ in range(M):
            op, a, b = get_line()
            if op == 0:
                _union(min(a, b), max(a, b), parents)
            else:
                if _check(a, b, parents):
                    print("YES")
                else:
                    print("NO")

    set_variable()


if __name__ == "__main__":
    main()

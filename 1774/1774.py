import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N, M = None, None
adj = None
pos = None
dist = None
parents = None
graph = None


def _union(a, b, parents):
    a, b = _find(a), _find(b)
    parents[max(a, b)] = min(a, b)


def _find(a):
    if parents[a] == a:
        return a
    else:
        parents[a] = _find(parents[a])
        return parents[a]


def set_variable():
    global N, M, adj, pos, dist, parents, graph
    N, M = get_line()
    pos = [None for _ in range(N + 1)]
    dist = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    graph = []
    parents = [i for i in range(N + 1)]
    for idx in range(1, N + 1):
        y, x = get_line()
        pos[idx] = (y, x)

    for i in range(1, N):
        for j in range(i + 1, N + 1):
            dist[i][j] = (
                (pos[i][0] - pos[j][0]) ** 2 + (pos[i][1] - pos[j][1]) ** 2
            ) ** 0.5
            graph.append((dist[i][j], i, j))
    graph.sort()
    for _ in range(M):
        st, ed = get_line()
        _union(st, ed, parents)


def solution():
    global N, M, adj, pos, dist, parents, graph
    answer = 0
    for now in graph:
        weight, i, j = now
        if not (_find(i) == _find(j)):
            _union(i, j, parents)
            answer += weight
    print(f"{answer:.2f}")


if __name__ == "__main__":
    set_variable()
    solution()

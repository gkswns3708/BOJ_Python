import sys
import heapq
from collections import deque


def solution(alp, cop, problems):
    answer = 0
    dist = [[sys.maxsize for _ in range(500)] for _ in range(500)]
    # heap = []
    # heapq.heappush(heap, (0, alp, cop))
    que = deque()
    dist[alp][cop] = 0
    max_alp, max_cop = 0, 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)
    que.append((0, alp, cop))
    while que:
        now_time, now_alp, now_cop, = que.popleft()
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if now_alp >= alp_req and now_cop >= cop_req:
                nxt_alp = now_alp + alp_rwd
                nxt_cop = now_cop + cop_rwd
                nxt_time = now_time + cost
                if dist[nxt_alp][nxt_cop] > nxt_time:
                    dist[nxt_alp][nxt_cop] = nxt_time
                    que.append((nxt_time, nxt_alp, nxt_cop))
        if dist[now_alp + 1][now_cop] > now_time + 1:
            dist[now_alp + 1][now_cop] = now_time + 1
            que.append((now_time + 1, now_alp + 1, now_cop))
        if dist[now_alp][now_cop + 1] > now_time + 1:
            dist[now_alp][now_cop + 1] = now_time + 1
            que.append((now_time + 1, now_alp, now_cop + 1))


alp = 10
cop = 10
problems = [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]

print(solution(alp, cop, problems))

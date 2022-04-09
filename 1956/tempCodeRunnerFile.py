eapq.heappop(heap)
            print(c, a, b, "weight, from , to")
            if a == b:
                return c
            else:
                for nxt_pos, weight in adj[b]:
                    print(nxt_pos, c + weight, "nxt_pos, weight")
                    if c + weight < dist[a][nxt_pos]:
                        dist[a][nxt_pos] = c + weight
                   
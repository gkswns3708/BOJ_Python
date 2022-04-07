
                        print(f'기존의 {nextpos}위치까지 {nowcost + nxtweight}원으로 가는 최소 시간은 {dist_dp[nextpos][nowcost + nxtweight]}초입니다.') 
                        print(f'이후의 {nextpos}위치까지 {nowcost + nxtweight}원으로 가는 최소 시간은 {dist_dp[nowpos][nowcost] + time}초입니다.') 
import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

W, H, X, Y, P = None, None, None, None, None
players = list()

def set_variable():
    global W, H, X, Y, P, players
    W, H, X, Y, P = get_line()
    for _ in range(P):
        x, y = get_line()
        players.append((x,y))

def solution():
    global W, H, X, Y, P, players
    def check(x, y):
        if  X <= x <= x + W and Y <= y <= H: # 중앙 사각형 내에 있을 경우
            return 1
        if (X - x) ** 2 + (Y + H/2 - y) ** 2 <= (H/2)**2:
            return 1
        if (X + W - x) ** 2 + (Y + H/2 - y) ** 2 <= (H/2)**2:
            return 1
        return 0
    
    answer = 0
    for x, y in players:
        answer += check(x,y)
    print(answer)



if __name__ == "__main__":
    set_variable()
    solution()

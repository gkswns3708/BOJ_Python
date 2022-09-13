import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())


def set_variable():
    pass


def solution():
    def d(i): 
        ret = i
        for i in str(i): # 15 => "15" =>(for)  => "1" , "5"
            ret += int(i)
        return ret
        # 9999 => d(9999) = 9999 + 9 + 9 + 9 + 9 = 10035
    
    answer_list = [True for _ in range(10000 + 2)] # list comprehension
    for i in range(1, 10001):
        now_num = d(i)
        if now_num<= 10000: 
            answer_list[now_num] = False

    for idx, i in enumerate(answer_list[1:10001]):
        if i:
            print(idx + 1)

if __name__ == "__main__":
    set_variable()
    solution()

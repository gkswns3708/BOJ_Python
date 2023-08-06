import sys
import math
from collections import defaultdict

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N = None
input_arr = None

def set_variable():
    global N, input_arr
    input_arr = []
    N = get_input()
    for _ in range(N):
        now_input = get_input()
        input_arr.append(now_input)


def solution():
    global N, input_arr
    def get_artihmetic_mean(arr):
        return round(sum(arr)/len(arr))
    def get_median(arr):
        return sorted(arr)[len(arr)//2]
    def get_Mode(arr):
        cnt_dict = defaultdict(int)
        for i in arr : cnt_dict[i] += 1
        max_value = max(cnt_dict.values())
        temp_list = [key for key, value in cnt_dict.items() if value == max_value]
        if len(temp_list) > 1:
            return sorted(temp_list)[1]
        else:
            return  temp_list[0]
    def get_min_max_gap(arr):
        return max(arr) - min(arr)
    print(get_artihmetic_mean(input_arr))
    print(get_median(input_arr))
    print(get_Mode(input_arr))
    print(get_min_max_gap(input_arr))
    
        
if __name__ == "__main__":
    set_variable()
    solution()
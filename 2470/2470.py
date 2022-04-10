import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline().strip())

N = None
arr = None


def set_variable():
    global N, arr
    N = get_input()
    arr = list(get_line())


def solution():
    global N, arr

    def TwoPointer():
        global N, arr
        left, right = 0, len(arr) - 1
        arr = sorted(arr)
        ans_l, ans_r = arr[left], arr[right]
        while left < right:
            summation = arr[left] + arr[right]
            if abs(summation) < abs(ans_l + ans_r):
                ans_l, ans_r = arr[left], arr[right]
            if summation > 0:
                right -= 1
            elif summation < 0:
                left += 1
            else:
                return ans_l, ans_r
        return ans_l, ans_r

    print(*TwoPointer())


if __name__ == "__main__":
    set_variable()
    solution()

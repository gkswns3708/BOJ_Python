def solution(survey, choices):
    answer = ""
    score = [0 for _ in range(4)]
    for sur, choi in zip(survey, choices):
        idx = None
        flag = True
        if sur == "RT" or sur == "TR":
            if sur == "TR":
                flag = False
            idx = 0
        elif sur == "CF" or sur == "FC":
            if sur == "FC":
                flag = False
            idx = 1
        elif sur == "JM" or sur == "MJ":
            if sur == "MJ":
                flag = False
            idx = 2
        elif sur == "AN" or sur == "NA":
            if sur == "NA":
                flag = False
            idx = 3
        now_score = choi - 4
        if flag == False:
            now_score *= -1
        score[idx] += now_score

    for idx, char in enumerate(["RT", "CF", "JM", "AN"]):
        answer += char[0] if score[idx] <= 0 else char[1]
    print(score)
    print(answer)

    return answer

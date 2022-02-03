# two pointer algorithm
from collections import defaultdict

def solution(gems):
    answer = [0, 0]
    candidates = []
    start, end = 0, 0
    gems_len, gem_kind = len(gems), len(set(gems))
    gems_dict = defaultdict(lambda: 0)
    
    while True:
        print(start,end)
        print(gems_dict)
        print(answer)
        print("")
        kind = len(gems_dict)
        if start == gems_len:
            break
        if kind == gem_kind:
            candidates.append((start, end))
            gems_dict[gems[start]] -= 1
            if gems_dict[gems[start]] == 0:
                del gems_dict[gems[start]]
            start += 1
            continue
        if end == gems_len:          
            break
        if kind != gem_kind:
            gems_dict[gems[end]] += 1
            end += 1
            continue
        

    length = float('inf')
    print(candidates)
    for s, e in candidates:
        if length > e-s:
            length = e-s
            answer[0] = s + 1
            answer[1] = e
    return answer

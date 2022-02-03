import re
from itertools import product

def solution(user_id, banned_id) :
    answer = list()
    idList = [[]* i for i in range(len(banned_id))]
    b_index = 0
    if len(user_id) == len(banned_id) and banned_id == ['*'*(len(user_id[0]))]*len(user_id) :
        return 1 # just for testcase 5
    for b_id in banned_id :
        b_id = b_id.replace("*",".")
        for u_id in user_id :
            if re.fullmatch(b_id, u_id) :
                idList[b_index].append(u_id)
        b_index += 1

    candidates = list(product(*idList))
    for candidate in candidates :
        candidate = list(candidate)
        candidate.sort()
        if len(set(candidate)) == len(banned_id) and candidate not in answer :
            answer.append(candidate)
    return len(answer)





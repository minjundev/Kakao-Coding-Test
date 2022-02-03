import re

def solution(p):
    answer = ''

    if not p :
        return answer

    u,v = secondStep(p)
    
    if isCorrect(u) :
        answer += u
        answer += solution(v)

    else :
        answer += '('
        answer += solution(v)
        answer += ')'
        u = u[1:-1]
        u = re.sub('[(]', '0', u)
        u = re.sub('[)]', '1', u)
        u = re.sub('0', ')', u)
        u = re.sub('1', '(', u)
        answer += u
        
    return answer

def secondStep(p) :
    u = ''
    v = ''
    flag = "default"
    cnt = 0
    
    while flag != 0 :
        if cnt == 0 :
            flag = 0
            
        if p[cnt] == '(' :
            flag += 1
        else :
            flag -= 1

        u += p[cnt]
        cnt += 1

        if cnt >= len(p) :
            break

    v = p[cnt:]
    return u, v

    
def isCorrect(p) :
    flag_correct = 0
    for i in range(0,len(p)) :
        if p[i] == '(' :
            flag_correct += 1
        else :
            flag_correct -= 1

        if flag_correct < 0 :
            return False

    if flag_correct == 0 :
        return True
    else :
        return False
    
            

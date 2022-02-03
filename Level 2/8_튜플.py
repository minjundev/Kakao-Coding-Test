import re

def solution(s):
    answer = []
    dict = {}
    s = re.sub('[{}]', '', s)
    s = s.split(',')
    
    
    while True :
        if len(s) == 0 :
            break
        if s[0] in dict :
            dict[s[0]] += 1
        else :
            dict[s[0]] = 1
        del s[0]

    while len(dict) > 0 :
        answer.append(int(max(dict, key=dict.get)))
        del dict[max(dict, key=dict.get)]
    
    
    return answer

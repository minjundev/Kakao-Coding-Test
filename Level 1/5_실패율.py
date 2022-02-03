import math

def solution(N, stages):
    answer = []
    failureRate = []

    stages.sort()
    
    for i in range(1,N+1) :
        if len(stages) == 0 :
            failureRate.append(0)
            continue
        cnt = stages.count(i)
        failureRate.append(cnt/len(stages))
        while i in stages :
            stages.remove(i)



    for i in range(1,N+1) :
        tmp = max(failureRate)
        index = failureRate.index(tmp)
        answer.append(index+1)
        failureRate[index] = -1
        
    
    return answer

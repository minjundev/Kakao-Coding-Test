from itertools import product

def solution(n, info):
    loseOrWin = [[] * 11 for i in range(11)]
    index = 0
    maxValue = -1
    finalCandidate = list()
    for i in range(11) :
        loseOrWin[i] = [k for k in range(info[i]+2)]
    print(loseOrWin)
    candidate = list(product(*loseOrWin))
    
    for index in range(len(candidate)-1, -1, -1) :
        if sum(candidate[index]) != n :
            del candidate[index]
            
    for i in range(len(candidate)) :
        diff = computeDiff(info,candidate[i])
        if diff > maxValue :
            maxValue = diff
            finalCandidate = [list(candidate[i])]
        elif diff == maxValue :
            finalCandidate.append(candidate[i])
        else :
            continue
    print(maxValue)
    print(finalCandidate)
    if maxValue <= 0 :
        return [-1]
    elif len(finalCandidate) == 1:
        return finalCandidate[0]

    else :
        return selectOne(10,finalCandidate)
                
            
        


def computeDiff(apeach,lion) :
    diff = 0
    for i in range(11) :
        if apeach[i] == 0 and lion[i] == 0 :
            continue
        elif apeach[i] >= lion[i] :
            diff -= 10-i
        else :
            diff += 10-i
    return diff


def selectOne(j, finalCandidate) :
    if j < 0 :
        return [-1]
    maxCount = 0
    indexList = list()
    for i in range(len(finalCandidate)) :
        if finalCandidate[i][j] == 0 :
            continue
        elif finalCandidate[i][j] > maxCount :
            maxCount = finalCandidate[i][j]
            indexList = [finalCandidate[i]]
        elif finalCandidate[i][j] == maxCount :
            indexList.append(finalCandidate[i])

    if len(indexList) == 1 :
        #print("if문")
        #print(indexList)
        return indexList[0]
    elif len(indexList) == 0 :
        #print("elif첫번째")
        return selectOne(j-1, finalCandidate)
    else :
        #print("elif두번째")
        return selectOne(j-1, indexList)
    

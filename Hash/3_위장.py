def solution(clothes):
    hashTable = dict()
    cases = list()
    for cloth in clothes :
        if cloth[1] not in hashTable :
            hashTable[cloth[1]] = [cloth[0]]
        else :
            hashTable[cloth[1]].append(cloth[0])
    for value in hashTable.values() :
        cases.append(len(value)+1)

    prod = 1
    for case in cases :
        prod *= case
    prod -= 1
    return prod

def solution(participant, completion) :
    tmp = 0
    hashTable = dict()
    for part in participant :
        hashTable[hash(part)] = part
        tmp += hash(part)
    for com in completion :
        tmp -= hash(com)
    return hashTable[tmp]

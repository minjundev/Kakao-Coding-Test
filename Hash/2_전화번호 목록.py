def solution(phone_book) :
    hashTable = dict()
    for pNumber in phone_book :
        hashTable[pNumber] = 1
    for pNumber in phone_book :
        for index in range(0,len(pNumber)) :
            if pNumber[:index] in hashTable :
                return False
    return True
        

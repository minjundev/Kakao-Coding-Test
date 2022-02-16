def solution(genres, plays):
    answer = list()
    hashTable = dict()
    index = 0
    for genre in genres :
        if genre not in hashTable :
            hashTable[genre] = [(index,plays[index])]
        else :
            hashTable[genre].append((index,plays[index]))
        index += 1

    for key, value in hashTable.items():
        sum = 0
        for val in value :
            sum += val[1]
        hashTable[key].append(sum)

    while len(hashTable) >= 1 :
        maxSum = 0
        maxGenre = ''
        for key, value in hashTable.items():
            sum = value[len(value)-1]
            if sum >= maxSum :
                maxSum = sum
                maxGenre = key
        del hashTable[maxGenre][len(hashTable[maxGenre])-1]
        hashTable[maxGenre].sort(key = lambda x : (-x[1], x[0]))
        if len(hashTable[maxGenre]) < 2:
            answer.append(hashTable[maxGenre][0][0])
        else :
            for index in range(2) :
                answer.append(hashTable[maxGenre][index][0])
        del hashTable[maxGenre]

    return answer

def solution(citations):
    citations.sort(reverse=True)
    numSet = [i for i in range(citations[0],-1,-1)]
    for num in numSet :
        tmp = len(list(filter(lambda x : x >= num, citations)))
        if tmp >= num :
            return num

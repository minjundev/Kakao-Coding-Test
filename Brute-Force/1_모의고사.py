def solution(answers):
    answerList = [0,0,0]
    first_answer = [1,2,3,4,5]*2000
    second_answer = [2,1,2,3,2,4,2,5]*1250
    third_answer = [3,3,1,1,2,2,4,4,5,5] * 1000
    index = 0
    for answer in answers :
        if first_answer[index] == answer :
            answerList[0] += 1
        if second_answer[index] == answer :
            answerList[1] += 1
        if third_answer[index] == answer :
            answerList[2] += 1
        index += 1

    maxIndex = 0
    person = [maxIndex]
    
    for index in range(1,3) :
        if answerList[index] > answerList[maxIndex] :
            maxIndex = index
            person = [maxIndex]
        elif answerList[index] == answerList[maxIndex] :
            person.append(index)
    
    return sorted(list(map(lambda x : x + 1, person)))

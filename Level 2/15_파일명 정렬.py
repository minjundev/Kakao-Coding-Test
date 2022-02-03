import re

def solution(files):
    answer = []
    solvingList = list()
    for i in range(len(files)) :
        files[i] = files[i].lower()

    for filesIndex in range(len(files)) :
        head = re.match('[\D]+',files[filesIndex]) # 처음부터 매칭
        number = re.search('[0-9]+',files[filesIndex]) # 있기만 하면 매칭
        tail = files[filesIndex][number.end():]
        solvingList.append((head[0],int(number[0][:5]),tail,filesIndex))

    solvingList.sort(key=lambda x : (x[0],x[1],x[3])) # main code

    for index in range(len(solvingList)) :
        answer.append(inputfiles[solvingList[index][3]])

    return answer

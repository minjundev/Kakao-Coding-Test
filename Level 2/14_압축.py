from string import ascii_uppercase

    
def solution(msg):
    answer = []
    solvingList = list(ascii_uppercase)
    LZWzip(msg,solvingList,answer)
    return answer




def LZWzip(msg,solvingList,answer) :
    w = ''
    c = ''
    if len(msg) == 1 :
        w = msg[0]
        length = 1
    else :
        for length in range(1, len(msg)+1) :
            if msg[0:length] in solvingList :
                w = msg[:length]
            else :
                length -= 1
                break
    answer.append(solvingList.index(w)+1)
    msg = msg[length:]
    if len(msg) > 0 :
        c = msg[0]
        solvingList.append(w+c)
        LZWzip(msg,solvingList,answer)
    else :
        return
    
    

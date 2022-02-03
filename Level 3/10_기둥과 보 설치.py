def isValid(answer):
    for x,y,a in answer:
        if a==0:
            if (x,y-1,0) in answer or (x-1,y,1) in answer or (x,y,1) in answer or y==0:
                continue
            else:
                return False
        if a==1:
            if (x,y-1,0) in answer or (x+1,y-1,0) in answer or ((x-1,y,1) in answer and (x+1,y,1) in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = set()
    for x,y,a,b in build_frame:
        if b==0:
            answer.remove((x,y,a))
            if not isValid(answer):
                answer.add((x,y,a))
        else:
            answer.add((x,y,a))
            if not isValid(answer):
                answer.remove((x,y,a))

    answer = [list(i) for i in answer]
    answer.sort(key=lambda x:(x[0],x[1],x[2]))
    return answer

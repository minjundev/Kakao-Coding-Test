def solution(record):
    answer = []
    dict = {}
    for rec in record :
        rec = rec.split(' ')
       
        if rec[0] == 'Enter' or rec[0] == 'Change':
            dict[rec[1]] = rec[2]
            
    for rec in record :
        tmpStr = ""
        rec = rec.split(' ')
        if rec[0] == 'Enter' :
            tmpStr = dict[rec[1]] + "님이 들어왔습니다."
            answer.append(tmpStr)
        elif rec[0] == 'Leave' :
            tmpStr = dict[rec[1]] + "님이 나갔습니다."
            answer.append(tmpStr)


    
    return answer

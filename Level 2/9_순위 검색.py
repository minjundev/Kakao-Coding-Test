def solution(info, query):
    answer = []
    for qry in query :
        cnt = 0
        validInfoIndexes = ['O' for index in range(0,len(info))]
        qry = qry.split(' ')

        for qr in qry :
            if qr == 'and' :
                continue
            elif qr == '-' :
                continue
            elif qr.isnumeric() :
                for info_index in range(0,len(info)) :
                    score = 0
                    if validInfoIndexes[info_index] == 'X' :
                        continue
                    
                    for each_index in range(len(info[info_index])) :
                        if info[info_index][each_index].isnumeric() :
                            score = info[info_index][each_index:]
                            break
                    if int(score) < int(qr) :
                        validInfoIndexes[info_index] = 'X'
                
            else :
                for index in range(0,len(info)) :
                    if validInfoIndexes[index] == 'X' :
                        continue
                    else :
                        if not (qr in info[index]) :
                            validInfoIndexes[index] = 'X'

        for flag in validInfoIndexes :
            if flag == 'O' :
                cnt += 1
        answer.append(cnt)
    return answer

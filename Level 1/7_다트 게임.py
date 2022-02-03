import math

def solution(dartResult):
    answer = 0
    dict = {'S' : 1, 'D' : 2, 'T' : 3}
    numList = [0,0,0]
    cnt = 0


    for i in range(0,3) :
        if dartResult[cnt] == '1' and dartResult[cnt+1] == '0' :
            numList[i] = 10
            cnt += 2

        elif dartResult[cnt].isnumeric() :
            numList[i] = int(dartResult[cnt])
            cnt += 1
            
            
        if dartResult[cnt] in dict :
            numList[i] = int(math.pow(numList[i], dict[dartResult[cnt]]))
            cnt += 1
         
        if cnt >= len(dartResult) :
            break
        
        
        if dartResult[cnt] == '*' :
            if i >= 1 :
                numList[i-1] *= 2
            numList[i] *= 2
            cnt += 1
          
        elif dartResult[cnt] == '#' :
            numList[i] *= -1
            cnt += 1
           
    
    for i in range(0,3) :
        answer += numList[i]
    
    return answer

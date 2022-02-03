def solution(s):
    answer = 0
    array = []
    array.append(s)

    
    for i in range(1,int(len(s)/2)+1) :
        cnt = 0
        tmp = ""
        token = s[:i]
        j = 0
        while j < len(s)+1 :
            if s[j:j+i] == token :
                cnt += 1
                j += i
            else :
                if cnt != 1 :
                    tmp += str(cnt) + token
                else :
                    tmp += token
                
                if(len(s) - j < len(token)) :
                    tmp += s[j:]
                    break
                token = s[j:j+i]
                cnt = 0

                continue
        array.append(tmp)


    for i in range(0,len(array)) :
        array[i] = len(array[i])

    answer = min(array)
    return answer

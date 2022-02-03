def solution(s):

    # for debug

    

    
    answer = ""

    cnt = 0

    while cnt < len(s) :
        
        if s[cnt].isnumeric() :
            answer = answer + s[cnt]
            cnt += 1
            continue

        if s[cnt] == "z" :
            answer = answer + "0"
            cnt += 4
            continue

        elif s[cnt] == "o" :
            answer = answer + "1"
            cnt += 3
            continue

        elif s[cnt] == "t" :
            if s[cnt+1] == "w" :
                answer = answer + "2"
                cnt += 3
                continue

            elif s[cnt+1] == "h" :
                answer = answer + "3"
                cnt += 5
                continue

            else :
                print("error")
                break

        elif s[cnt] == "f" :
            if s[cnt+1] == "o" :
                answer = answer + "4"
                cnt += 4
                continue

            elif s[cnt+1] == "i" :
                answer = answer + "5"
                cnt += 4
                continue

            else :
                print("error")
                break



        elif s[cnt] == "s" :
            if s[cnt+1] == "i" :
                answer = answer + "6"
                cnt += 3
                continue

            elif s[cnt+1] == "e" :
                answer = answer + "7"
                cnt += 5
                continue

            else :
                print("error")
                break

        elif s[cnt] == "e" :
            answer = answer + "8"
            cnt += 5
            continue

        elif s[cnt] == "n" :
            answer = answer + "9"
            cnt += 4
            continue


    answer = int(answer)
    return answer

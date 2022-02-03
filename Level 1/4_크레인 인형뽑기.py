def solution(board, moves):
    answer = 0
    stack = []
    picked = 0

    
    for m in moves :
        for i in range (0,len(board)) :
            if board[i][m-1] == 0 :
                continue
            else :
                picked = board[i][m-1]
                stack.append(picked)
                board[i][m-1] = 0
                break
            
        stackLen = len(stack)

        if stackLen >= 2 :
            if stack[stackLen-1] == stack[stackLen-2] :
                stack = stack[:-2]
                answer += 2

    return answer

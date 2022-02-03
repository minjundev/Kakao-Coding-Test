def solution(m, n, board):
    global change
    change = True
    answer = 0
    board = stringListTo2dList(m,n,board)
    
    while change :
        change = False
        dictionary = dict()
        for curr_row in range(1,m) :
            for curr_col in range(1,n) :
                isMatched(curr_row, curr_col, board, dictionary)
        answer += len(dictionary)

        fillToO(board,dictionary)

        for curr_row in range(0,m) :
            for curr_col in range(0,n) :
                fall(curr_row, curr_col,board, dictionary)
        
    return answer

def stringListTo2dList(m,n,board) :
    tmp_list = [[]*m for _ in range(n)]
    for i in range(m) :
        for j in range(n) :
            tmp_list[i].append(board[i][j])
    return tmp_list


def isMatched(row, col, board, dictionary) :
    global change
    if board[row-1][col-1] == '0' or board[row-1][col] == '0' or board[row][col-1] == '0' or board[row][col] == '0' :
        return False
    elif board[row-1][col-1] == board[row-1][col] == board[row][col-1] == board[row][col] :
        for i in range(row-1,row+1) :
            for j in range(col-1, col+1) :
                dictionary[i,j] = 1
        change = True
        return True
    
    else :
        return False

def fillToO(board, dictionary) :
    for key in dictionary :
        board[key[0]][key[1]] = '0'

def fall(row,col,board, dictionary) :
    global change
    if (row+1,col) in dictionary :
        for i in range(row,-1,-1) :
                board[i+1][col] = board[i][col]
        board[0][col] = '0'
        change = True

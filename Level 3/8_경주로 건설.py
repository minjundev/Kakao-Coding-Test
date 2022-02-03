from collections import deque

def solution(board):
    global N, check, new_board, answer
    answer = []
    N = len(board)
    new_board = [board[i][:] for i in range(N)]
    bfs(0, 0, 0, 'R')
    bfs(0, 0, 0, 'D')
    return min(answer)

def calc_cost(cur_dir, nex_dir, cost):
    if (cur_dir == 'R' or cur_dir == 'L') and (nex_dir == 'L' or nex_dir == 'R'):  
        return cost + 100
    if (cur_dir == 'D' or cur_dir == 'U') and (nex_dir == 'D' or nex_dir == 'U'):  
        return cost + 100
    if (cur_dir == 'R' or cur_dir == 'L') and (nex_dir == 'D' or nex_dir == 'U'):  
        return cost + 600
    if (cur_dir == 'D' or cur_dir == 'U') and (nex_dir == 'R' or nex_dir == 'L'):  
        return cost + 600

    
def bfs(x, y, cost, direct):
    queue = deque([(x, y, cost, direct)])
    check = [[0 for _ in range(N)] for _ in range(N)]
    check[x][y] = 1
    while queue:
        print(queue)
        print("check : ", check)
        print("")
        x, y, cost, cur_dir = queue.popleft()
        if x == N-1 and y == N-1:
            answer.append(cost)
            continue
        for i, j, d in (0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L'), (-1, 0, 'U'):
            new_x, new_y, new_cost = x+i, y+j, calc_cost(cur_dir, d, cost)
            if new_x < 0 or new_y < 0 or new_x >= N or new_y >= N:
                continue
            if not new_board[new_x][new_y]:
                if not check[new_x][new_y] or check[new_x][new_y] > new_cost:
                    check[new_x][new_y] = new_cost
                    queue.append((new_x, new_y, new_cost, d))
    


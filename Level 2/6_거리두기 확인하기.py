def solution(places):
    answer = []
    for place in places :
        mainAlgorithm(answer,place)
    return answer


def mainAlgorithm(answer, place):
    for curr_row in range(5) :
            for curr_col in range(5) :
                if place[curr_row][curr_col] == 'P' :
                    for next_row in range(curr_row,5) :
                        for next_col in range(0,5) :
                            length = "default"
                            if place[next_row][next_col] == 'P' and (curr_row,curr_col) != (next_row,next_col) and (curr_row,curr_col) < (next_row,next_col):
                                length = abs(next_row - curr_row) + abs(next_col - curr_col)
                                if length < 2 :
                                    answer.append(0)
                                    return answer
                                elif length == 2 :
                                    if curr_row == next_row :
                                        if place[curr_row][curr_col+1] != 'X':
                                            answer.append(0)
                                            return answer
                                    elif curr_col == next_col :
                                        if place[curr_row+1][curr_col] != 'X':
                                            answer.append(0)
                                            return answer
                                    else :
                                        if curr_col < next_col :
                                            if place[curr_row][curr_col+1] != 'X' or place[curr_row+1][curr_col] != 'X' :
                                                answer.append(0)
                                                return answer
                                        else :
                                            if place[curr_row][curr_col-1] != 'X' or place[curr_row+1][curr_col] != 'X' :
                                                answer.append(0)
                                                return answer
    answer.append(1)
    return answer

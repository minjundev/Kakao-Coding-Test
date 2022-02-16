def solution(array, commands):
    answer = list()
    for cmd in commands :
        [i,j,k] = cmd
        new_arr = sorted(array[i-1:j])
        answer.append(new_arr[k-1])
    return answer

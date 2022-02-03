def solution(n, arr1, arr2):
    answer = []
    

    for i in range(0,n) :
        tmp = ""
        tmp += binary(n,bin(arr1[i]|arr2[i])[2:])
        tmp = tmp.replace('1', '#')
        tmp = tmp.replace('0', ' ')
        answer.append(tmp)
        
    return answer


def binary(n, bin) :
    for i in range (len(bin), n) :
        bin = '0' + bin
    return bin

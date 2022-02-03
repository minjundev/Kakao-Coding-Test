def solution(n, t, m, p):
    answer = ''
    number = 0
    while len(answer) < t*m :
        answer += decimalToN(number,n)
        number += 1
    return answer[p-1:(p-1)+m*t:m]

def decimalToN(number, n) :
    T = "0123456789ABCDEF"
    q,r = divmod(number,n)
    return decimalToN(q,n) + T[r] if q else T[r]

def solution(n, k):
    return list(map(isPrimeNumber,decimalToN(n,k).split('0'))).count(True)

def decimalToN(number, n) :
    T = "0123456789ABCDEF"
    q,r = divmod(number,n)
    return decimalToN(q,n) + T[r] if q else T[r]

def isPrimeNumber(number) :
    if not number :
        return False
    number = int(number)
    if number == 1 :
        return False
    for i in range(2,int((number+1)**0.5)+1) :
        if number % i == 0 :
            return False
    return True

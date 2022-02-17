from itertools import permutations

def solution(numbers):
    answer = list()
    numbers = list(numbers)
    for i in range(1,len(numbers)+1) :
        answer += list(filter(isPrimeNumber,(list(map(int,list(map(''.join,list(permutations(numbers,i)))))))))
    return len(set(answer))

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

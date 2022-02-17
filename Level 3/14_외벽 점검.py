import math

def solution(n, weak, dist):
    if dist[-1] >= n:
        return 1
    answer = detect(n, weak, dist)    
    if answer < 0 :
        return -1
    return answer

def detect(n, weak, dist):
    if not weak:
        return 0
    if not dist:
        return -math.inf
    return 1 + min(detect(n,newWeak(n, weak, dist, -1),dist[:-1]), detect(n,newWeak(n, weak, dist, 1),dist[:-1]))

def newWeak(n, weak, dist, direction):
    d = dist[-1]
    w = weak[-1]
    print('d= ',d,'w= ',w)
    copy_weak = weak.copy()
    detectedList = list()
    
    if direction < 0: #left
        target = encoding(n,w-d)
        while w != target :
            detectedList.append(encoding(n,w))
            w = encoding(n,w-1)
    else : #right
        target = encoding(n,w+d)
        while w != target :
            detectedList.append(encoding(n,w))
            w = encoding(n,w+1)
    print(list(filter(lambda x : x not in detectedList, weak)))
    return list(filter(lambda x : x not in detectedList, weak))
            


def encoding(n,number):
    while number >= n :
        number -= n
    while number < 0 :
        number += n
    return number


            

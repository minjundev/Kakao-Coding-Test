from copy import deepcopy

def rotate(key):
    M = len(key)
    return [[key[M-1-i][j] for i in range(M)] for j in range(M)]

def can_open(key,lock):
    N, M = len(lock), len(key)
    for dr in range(-N+1,N,1):
        for dc in range(-N+1,N,1):
            lock_copy = deepcopy(lock)
            for r in range(M):
                for c in range(M):
                    if 0<=r+dr<=N-1 and 0<=c+dc<=N-1:
                        lock_copy[r+dr][c+dc] += key[r][c]
            if lock_copy == [[1 for _ in range(N)] for _ in range(N)]:
                return True
    return False

def solution(key,lock):
    if can_open(key,lock) == True:
            return True
    for _ in range(3):
        key = rotate(key)
        if can_open(key,lock) == True:
            return True
    return False

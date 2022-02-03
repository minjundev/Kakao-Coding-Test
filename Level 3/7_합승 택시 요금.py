import sys
INF = sys.maxsize

def solution(n, s, a, b, fares):
    fares = floyd_Warshall(n,fares)
    answer = list()
    for k in range(n) :
        answer.append(fares[s-1][k] + fares[k][a-1] + fares[k][b-1])
    return min(fares[s-1][a-1] + fares[s-1][b-1],min(answer))


def floyd_Warshall(n,fares) :
    dist = [[INF]* n for i in range(n)]
    for fare in fares :
        dist[fare[0]-1][fare[1]-1] = fare[2]
        dist[fare[1]-1][fare[0]-1] = fare[2]

    #[i,j] vs [i,k] + [k+j]
    for k in range(n) : 
        for i in range(n) : 
            for j in range(n) :
                if dist[i][j] > dist[i][k] + dist[k][j] :
                    dist[i][j] = dist[i][k] + dist[k][j]

    for i in range(n) :
        dist[i][i] = 0
    return dist

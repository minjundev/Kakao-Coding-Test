def solution(lines):

    #get input
    S , E= [], [] 
    totalLines = 0 
    for line in lines:
        totalLines += 1
        type(line)
        (d,s,t) = line.split(" ")

       ##time to float
        t = float(t[0:-1])
        (hh, mm, ss) = s.split(":")
        seconds = float(hh) * 3600 + float(mm) * 60 + float(ss)

        E.append(seconds + 1)
        S.append(seconds - t + 0.001)
    #print(E)
    #print(S)
    #count the maxTraffic
    S.sort()


    curTraffic = 0
    maxTraffic = 0
    countE = 0
    countS = 0
    while((countE < totalLines) & (countS < totalLines)):
        print(countS,countE)
        if(S[countS] < E[countE]):
            curTraffic += 1
            maxTraffic = max(maxTraffic, curTraffic)
            countS += 1
        else: ## it means that a line is over.
            curTraffic -= 1
            countE += 1

    return maxTraffic

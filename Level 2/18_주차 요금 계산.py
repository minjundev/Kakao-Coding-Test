import math

def solution(fees, records):
    answer = []
    inDict = dict()
    outDict = dict()
    
    for record in records :
        splitedRecord = record.split(' ')
        if splitedRecord[2] == 'IN' :
            inDict[splitedRecord[1]] = splitedRecord[0]
        else :
            if splitedRecord[1] not in outDict :
                outDict[splitedRecord[1]] = computeMinute(inDict[splitedRecord[1]],splitedRecord[0])
            else :
                outDict[splitedRecord[1]] += computeMinute(inDict[splitedRecord[1]],splitedRecord[0])
            del inDict[splitedRecord[1]]

    for key,value in inDict.items() :
        if key not in outDict :
            outDict[key] = computeMinute(inDict[key],'23:59')
        else :
            outDict[key] += computeMinute(inDict[key],'23:59')

    outDict = dict(sorted(outDict.items()))

    for key,value in outDict.items() :
        answer.append(computePrice(fees[1],value,fees[0],fees[2],fees[3]))
    
    return answer

def computeMinute(start,end) :
    tmp_start = start.split(':')
    tmp_end = end.split(':')
    return (int(tmp_end[0])-int(tmp_start[0]))*60 + (int(tmp_end[1])-int(tmp_start[1]))

def computePrice(basicPrice,accumulatedTime,basicTime,unitTime,unitPrice) :
    if accumulatedTime-basicTime  < 0 :
        return basicPrice
    else :
        return basicPrice + math.ceil((accumulatedTime-basicTime)/unitTime)*unitPrice

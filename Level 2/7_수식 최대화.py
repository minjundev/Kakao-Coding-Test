from itertools import permutations

def solution(expression):
    answer = 0
    index = 0
    operators = []
    answerList = []
    splitedExp = []
    splitedExpression = []
    tmpValue = ""
    changeFlag = 0

    if '+' in expression :
        operators.append('+')
    if '-' in expression :
        operators.append('-')
    if '*' in expression :
        operators.append('*')
  
    operators = list(permutations((operators),len(operators)))

    while index < len(expression) :
        if expression[index].isnumeric() :        
            tmpValue += expression[index]
            if index == len(expression) -1 :
                splitedExpression.append(tmpValue)
            
        else :
            splitedExpression.append(tmpValue)
            tmpValue = ""
            splitedExpression.append(expression[index])
        index += 1

    
    splitedExp = splitedExpression[:]

    for operator in operators :
        splitedExp = splitedExpression[:]
        while len(splitedExp) > 1 :
            for i in range (len(operator)) :
                j = 0
                while True :
                    tmpValue = 0
                    changeFlag = 0
                    if splitedExp[j] == operator[i] :
                        if operator[i] == '+' :
                            tmpValue = int(splitedExp[j-1]) + int(splitedExp[j+1])
                            splitedExp[j-1] = tmpValue
                            del splitedExp[j:j+2]
                            changeFlag = 1
                        elif operator[i] == '*' :
                            tmpValue = int(splitedExp[j-1]) * int(splitedExp[j+1])
                            splitedExp[j-1] = tmpValue
                            del splitedExp[j:j+2]
                            changeFlag = 1
                        elif operator[i] == '-' :
                            tmpValue = int(splitedExp[j-1]) - int(splitedExp[j+1])
                            splitedExp[j-1] = tmpValue
                            del splitedExp[j:j+2]
                            changeFlag = 1
                    j += 1
                    if changeFlag == 1:
                        j = 0
                    elif j >= len(splitedExp) and changeFlag == 0 :
                        break
                    
        answerList.append(int(abs(splitedExp[0])))

    answer = max(answerList)
    return answer

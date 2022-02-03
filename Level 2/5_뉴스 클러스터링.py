def solution(str1, str2):
    list1 = makeList(str1)
    list2 = makeList(str2)

    if len(list1) + len(list2) == 0 :
        return 65536

    list1_copy = list1.copy()
    list2_copy = list2.copy()

    intersection = []
    for list1_content in list1 :
        if list1_content in list2_copy :
            intersection.append(list1_content)
            list1_copy.remove(list1_content)
            list2_copy.remove(list1_content)

    union = list1_copy + list2_copy + intersection
    answer = int((len(intersection) / len(union)) * 65536)
    return answer



def makeList(strN) :
    strN = strN.upper()
    answer = []
    for index in range(len(strN) - 1) :
        if strN[index: index+2].isalpha() :
            answer.append(strN[index:index+2])
    return answer

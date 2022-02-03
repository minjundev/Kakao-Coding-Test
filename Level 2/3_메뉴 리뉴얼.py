from itertools import combinations
from collections import Counter

def solution(orders,course) :
    answer = []
    for c in course :
        order_combi = []
        for order in orders :
            for combi in combinations(order, c) :
                order_combi.append(''.join(sorted(combi)))

        order_count = Counter(order_combi).most_common()
        print(order_count)
        max = 0
        for oc in order_count :
            if oc[1] >= max :
                max = oc[1]

        for oc in order_count :
            if oc[1] >= max and oc[1] != 1 :
                answer.append(oc[0])
    return sorted(answer)
                

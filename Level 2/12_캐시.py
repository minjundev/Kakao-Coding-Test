def solution(cacheSize, cities):
    answer = 0
    dictionary = dict()
    if cacheSize == 0:
        return 5*len(cities)
    for city in cities :
        city = city.lower()
        answer += LRUalgorithm(cacheSize, city, dictionary)
    return answer

def LRUalgorithm(cacheSize, city, dictionary) :
    for key in dictionary :
        dictionary[key] += 1
        
    if city in dictionary :
        dictionary[city] = 0
        return 1

    if len(dictionary) >= cacheSize:
        dictionary.pop(max(dictionary,key=dictionary.get))
    dictionary[city] = 0       
    return 5
        
    

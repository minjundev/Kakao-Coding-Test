import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    pre = list()
    post = list()
    for i in range (0,len(nodeinfo)) :
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key=lambda x : x[1], reverse = True)
    nodeinfo_copy_1 = nodeinfo.copy()
    nodeinfo_copy_2 = nodeinfo.copy()
    preorder(nodeinfo_copy_1,pre)
    postorder(nodeinfo_copy_2,post)
    return [pre,post]
    
def preorder(nodeinfo,aList) :
    if not nodeinfo :
        pass
    else :
        aList.append(nodeinfo[0][2])
        root = nodeinfo.pop(0)
        left = list(filter(lambda x : x[0] < root[0] , nodeinfo))
        right = list(filter(lambda x : x[0] > root[0] , nodeinfo))
        preorder(left,aList)
        preorder(right,aList)

def postorder(nodeinfo,aList) :
    if not nodeinfo :
        pass
    else :
        root = nodeinfo[0]
        left = list(filter(lambda x : x[0] < root[0] , nodeinfo))
        right = list(filter(lambda x : x[0] > root[0] , nodeinfo))
        postorder(left,aList)
        postorder(right,aList)
        aList.append(root[2])
        nodeinfo.pop(0)

        
    

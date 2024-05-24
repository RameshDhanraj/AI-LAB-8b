import math

def minmax(currDepth,nodeIndex,maxTurn,scores,targetDepth):
    if currDepth == targetDepth:
        return scores[nodeIndex]
    if maxTurn:
        return max(
            minmax(currDepth+1,nodeIndex*2,False,scores,targetDepth - 1),
            minmax(currDepth+1,nodeIndex*2 + 1,False,scores,targetDepth - 1),
        )
    else:
        return min(
            minmax(currDepth+1,nodeIndex*2,True,scores,targetDepth - 1),
            minmax(currDepth+1,nodeIndex*2 + 1,True,scores,targetDepth - 1),
        )

if __name__ == '__main__':
    scores = [
        10,-3,-19,11,11,0,-2,-2,-2,14,-16,2,17,15,-14,15,-15,13,-19,-9,4,-9,2,9,-14,2,-18
    ]
    treeLength = int(math.log2(len(scores)))
    optimalValue = minmax(0,0,True,scores,treeLength)
    print("The optimal Move for Maximizing Player ",optimalValue)
def partitions(n,sequenceList=None):
    """
    n integer greater than 0.`
    """
    OP = [1] + [0]*n
    if not sequenceList:
        sequenceList = generatePMList(n)

    for i in range(1,n+1):
        OP[i] = sum(listMultiply( OP[:i],sequenceList[n-i:]))
    return OP[-1]

def listMultiply(L1,L2):
    """
    length of L1 and L2 must be the same.
    """
    N = len(L1)
    OP = [0]*N
    for i in range(N):
        OP[i] = L1[i] * L2[i]
    return OP

def generatePMList(N):
    OP = [0]*N
    OP[0] = 1
    nextOptions = [1,3]
    value = 1
    step = 0
    optionIndex = 0
    nextPosition = 0 + nextOptions[optionIndex]
    
    while nextPosition < N:
        OP[nextPosition] = value
        
        if optionIndex == 0:
            nextOptions[0] += 1
        elif optionIndex == 1:
            nextOptions[1] += 2

        step += 1
        
        if (step+1)%4 == 0 or (step+1)%4 == 2:
            value *= -1

        optionIndex = int((step%2))
        nextPosition += nextOptions[optionIndex]

    OP.reverse()        
    return OP

"""
Daniil Yarrovi

Solution for challenge #370 from r/dailyprogrammer
"""
def upc(number):
    """
    Takes a int number.
    Returns M the 12th number for UFC
    """
    n = len(str(number))
    if n < 11:
        #Needs 11 digits
        padding = 11 - n
    else:
        padding = 0
        
    numList = [0]*padding + [int(x) for x in str(number)]
    n = len(numList)

    OP = 0

    for i in range(0,n,2):
        #step 1
        OP += numList[i]

    #step 2
    OP *= 3
    for i in range(1,n,2):
        #step 3
        OP += numList[i]

    #step 4
    M = OP%10

    #step 5
    if M == 0:
        pass
    else:
        M = 10 - M

    return M

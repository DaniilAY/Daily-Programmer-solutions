"""
Daniil Yarrovi

Solution to r/dailyprogrammer #378
"""
def addThreholds(taxRate):
    """
    taxRate is a List of Lists.
    Each list holds income cap and marginal tax rate.
    Each theshhold is represented as List within taxRate

    What this function does is add the total tax accrued through the previous
    tax tiers.
    """
    taxSum = 0
    taxRate[0].append(taxSum)

    n = len(taxRate)
    for i in range(1,n):
        if i < 2:
            low = 0
        else:
            low = taxRate[i-2][0]
        high = taxRate[i-1][0]
        bracket = high - low
        taxSum += bracket*taxRate[i-1][1]
        taxRate[i].append(taxSum)

    return taxRate

def tax(earned,rates):
    """
    earned is the taxable amount.
    rates are a list of list.
    Each index of the list reprents tax bracket.
    Each tax bracket is reprented as a list of two values
    first being income cap, the second being marginal tax rate
    """
    taxRate = addThreholds(rates)
    n = len(taxRate)
    OP = 0
    
    for i in range(n):
        if earned > taxRate[i][0]:
            pass
        else:
            break
    if i > 0:
        print(taxRate[i][2])
        OP = taxRate[i][2] + (earned-taxRate[i-1][0])*taxRate[i][1]
    return int(OP)

if __name__ == "__main__":
    q = [[10000,0],[30000,0.1],[100000,0.25],[-1,0.4]]
    w = addThreholds(q)
    print(w)
    print(tax(1234567,q))

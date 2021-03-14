"""
Daniil Yarrovi
Solution r/dailyprogrammer #378
"""
def HavelHakimi(seq):
    """
    This function takes seq, a list where each value is a integer.
    Each value in hte list represents a person and the number of people they
    know in the list.
    The function returns True if seq is valid, False otherwise
    """
    seq.sort()
    seq.reverse()

    while seq and seq[-1] == 0:
        """
        seq is checking if there are elements in the list before indexing
        """
        seq.pop()


    while seq:
        seq.sort()
        n = len(seq)
        value = seq[-1]

        if value > n - 1:
            return False
        else:
            seq.pop()
            
            for i in range(1,value+1):
                i *= -1
                seq[i] -= 1
            
    return True
        
if __name__ == "__main__":
    #print(HavelHakimi([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]))
    print(HavelHakimi([3, 1, 2, 3, 1, 0]))

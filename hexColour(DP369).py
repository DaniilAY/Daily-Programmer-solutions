"""
Daniil Yarrovi

Solution Challenge #369 from r/dailyprogrammer
"""
def hexcolour(red,green,blue):
    """
    Takes 3 int values red, green and blue.
    Each respresents values ranging between 0-255

    It then returns the colour as hex
    """
    OP = "#"
    rgb = [red,green,blue]

    for i in range(len(rgb)):
        hexString = hex(rgb[i])[2:]
        if len(hexString) < 2:
            hexString = "0" + hexString
        OP += hexString

    return OP.upper()

def blend(colour1,colour2):
    """
    Takes two colours and averages red, green and blue
    Each colour is in hex.

    rgb is a list representing red green and blue.
    """
    OP = "#"
    
    rgb = [0]*3

    for i in range(0,3):
        #Gets the average of red,green and blue.
        str1 = colour1[2*i+1:2*i+3]
        str2 = colour2[2*i+1:2*i+3]
        rgb[i] = round( (int(str1,16) + int(str2,16))/2 )

    return hexcolour(rgb[0],rgb[1],rgb[2])

    

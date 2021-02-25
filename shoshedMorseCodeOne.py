def morseDictionary():
    z= ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()
    OP = {}
    for i in range(97,123):
        index = i - 97
        OP[chr(i)] = z[index]
    return OP

def revMorseDictionary():
    z= ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()
    OP = {}
    for i in range(97,123):
        index = i - 97
        OP[z[index]] = chr(i)
    return OP

def smoshedMorse(word):
    MD = morseDictionary()

    OP = ""
    for i in word:
        OP += MD[i]

    return OP

def alphabetPermutation(morse):
    revDictionary = revMorseDictionary()
    dictionary = morseDictionary()
    word = ""
    indexList = [1]*26
    index = 0
    while morse:
        if indexList[index] > 4:
            indexList[index] = 1
                    
            oldLetter = word[-1]
            word = word[:-1]
            morse = dictionary[oldLetter] + morse

            index -= 1
            indexList[index] += 1

        else:
            morseLen = indexList[index]
            try:
                letter = revDictionary[morse[:morseLen]]
                if letter in word:
                    indexList[index] += 1

                else:
                    word += letter
                    morse = morse[morseLen:]
                    index += 1
            except KeyError:
                indexList[index] += 1
        print("\n word : "+word+"\n morse : "+morse)
        print("index :"+ str(index))
        print("word length :" +str(len(word)))
    return word
        
    

    
    

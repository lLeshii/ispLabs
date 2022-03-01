import statistics


def clean_word(oldWord):
    length = len(oldWord)
    endSent = False
    symbPos = 0
    for i in oldWord:
        if symbPos <= length-1:
            if i == "," or i == ";" or i == "\"" or i == "\'" \
                    or i == ":" or i == "(" or i == ")" or i == "?" \
                    or i == "!":
                if i == ";" or i == "?" or i == "!":
                    endSent = True
                length -= 1
                oldWord = oldWord[:symbPos] + oldWord[symbPos+1:]
            elif (i == "." and oldWord[symbPos-1].islower()) or\
                    (i == "." and oldWord[symbPos-1].isnumeric()):
                if(symbPos <= length-2 and oldWord[symbPos+1] == "." and oldWord[symbPos+2] == "." ):
                    length -= 3
                    oldWord = oldWord[:symbPos] + oldWord[symbPos + 3:]
                else:
                    length -= 1
                    oldWord = oldWord[:symbPos] + oldWord[symbPos+1:]
                endSent = True
            elif(i == "—"):
                oldWord = ""
                symbPos = length+1
            else:
                symbPos += 1
    return [oldWord, endSent]


def clean_text(oldlist):
    j = 0
    s = 0
    newlist = []
    numlist = []
    for i in oldlist:
        startlist = clean_word(i)
        newlist.append(startlist[0])
        if startlist[1]:
           numlist.append(s+1)
           s = 0
        else:
            s += 1
        if newlist[j] == "":
            newlist.pop(j)
        else:
            j += 1
    return [newlist, numlist]


def wordCount(rawDict):
    ownDict = {}
    for i in rawDict:
        if i in ownDict.keys():
            ownDict[i] += 1
        else:
            ownDict[i] = 1
    return ownDict

def symbCount(nSymb, specDict):
    nDict = {}
    for i in specDict.keys():
        if len(i) >= nSymb:
            k = i
            n = 0
            m = nSymb
            for z in range(len(i) - nSymb+1):
                proto = k[n:m]
                if proto in nDict.keys():
                    nDict[proto] += specDict[i]
                else:
                    nDict[proto] = specDict[i]
                n += 1
                m += 1
    return nDict


def startAnalysis(nSymb, mSymb):
    if nSymb == 0:
        nSymb = 4
    if mSymb == 0:
        mSymb = 10
    file = open("testText", "r")
    str1 = file.read()
    str1 = str1.replace("\n", " ").replace("'ll", " will").replace("'m", " am").replace("'s", " is").replace("'re", " are").\
        replace("won't", "would not").replace("n't", " not")
    rawList = str1.split(" ")
    newList = clean_text(rawList)
    newList.append(wordCount(newList[0]))
    newList.append(symbCount(nSymb, newList[2]))
    print(f"Arithmetic mean of words in sentences: {int(sum(newList[1]) / len(newList[1]))}\n")
    print(f"Median value of words in sentences: {statistics.median(newList[1])} [{newList[1][(int((len(newList[1]) + 1)/2))]}]\n\n")
    print("WORD RATING:\n")
    for key, value in newList[2].items():
        print(key, '-->', value)
    print("SYMBOL RATING:\n")
    list_d = list(newList[3].items())
    list_d.sort(reverse = True, key=lambda i: i[1])
    i = 0
    for key, value in list_d:
        if(i < mSymb):
            print(f"\t{key}--|--{value}")
            i += 1
        else:
            break
    return 0


def startData():
    print("Input N in n-grams for counting: ")
    nSymb = int(input())
    print("Input M in top-m for counting: ")
    mSymb = int(input())
    startAnalysis(nSymb, mSymb)
    return 0


startData()
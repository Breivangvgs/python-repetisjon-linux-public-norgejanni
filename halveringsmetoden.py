import random

playing = True

def ogList(maxNumber):
    leList = []
    for i in range(1,maxNumber+1):
        leList.append(i)
    return leList

def rightOrWrong(guess, currentList):
    feedback = input("HIGHER, LOWER OR CORRECT?")
    if feedback.lower().startswith("c"):
        print("LETSGOOOO")
    elif feedback.lower().startswith("h"):
        del currentList[0:guess]
    elif feedback.lower().startswith("l"):
        del currentList[guess-1:-1]
    return currentList


while playing:
    print("GUESS THE NUMBER")
    maxNum = int(input("INSERT RANGE: 1-"))
    numList = ogList(maxNum)
    print(numList)
    while True:
        guess = numList[int(len(numList)/2)]
        print(f"MY GUESS IS {guess}")
        numList = rightOrWrong(guess, numList)
        print(numList)
    
    
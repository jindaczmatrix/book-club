import random

def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]

    return res

print(generateOne(28))

def score(goal, testString):
    numsSame = 0
    for i in range(len(goal)):
        if goal[i] == testString[i]:
            numsSame += 1
    return numsSame / len(goal)

def main():
    goalString = "methinks it is like a weasel"
    newString = generateOne(28)
    best = 0
    newScore = score(goalString, newString)
    while score(goalString, newString) < 1:
        if newScore >= best:
            print(newScore, newString)
            best = newScore
        newString = generateOne(28)
        newScore = score(goalString, newString)

main()


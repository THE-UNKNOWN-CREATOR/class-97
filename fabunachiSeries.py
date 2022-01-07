times = 10

fibunachii = []
currentNumber, previousNum = 0, 1

fibunachii.append(currentNumber)
for i in range(times) :
    nextNum = currentNumber + previousNum
    previousNum = currentNumber
    currentNumber = nextNum
    fibunachii.append(currentNumber)

print(fibunachii)
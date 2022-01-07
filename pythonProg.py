word = input("Enter a word ")

letterCount = 0
wordCount = 1

for l in word :
    letterCount += 1
    if (l == ' '):
        wordCount += 1

print(f"The number of letters are {letterCount} and the number of words are {wordCount}")
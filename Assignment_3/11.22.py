#Elaine Wilde 1671617

wordinput = input()

wordsplit= wordinput.split(" ")

worddict = {

}

for i in wordsplit:
    if i in worddict:
       worddict [i] += 1
    else:
        worddict [i] = 1

for i in wordsplit:
    print(i, worddict[i])


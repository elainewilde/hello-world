#Elaine Wilde 1671617

enter_word = input()
outpt_word = ''

new_word = enter_word.strip(enter_word)
new_word = enter_word.replace(" ", "")

word_length = len(new_word)

flag = True

# loops with explicit syntax = index, header, incrementer
# loops and indexing: positive and negative indexing (moving forwards and backwards), and starting position (at beginning, at end)

index = 0 #starts at zero and moves through the string
while index < word_length: #starts at 0 and continues while in length of word
    compare_boolean = (new_word[ 0 + index] == new_word[(word_length - 1) - index]) #is True if letters match
    flag *= compare_boolean #if letters don't match then false, one false means it will be zero, stays zero
    index += 1

if flag == True:
    print(enter_word, "is a palindrome")

if flag == False:
    print(enter_word, "is not a palindrome")

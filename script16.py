welcome = 'Welcome to the English to pig Latin translator!'
print welcome
pyg = 'ay'

original = raw_input("What's your word?>> ")
word = original.lower()
first = word[0]

if len(original) != 0 and original.isalpha():
    if first in ('a', 'e', 'i', 'o', 'u'):
        new_word = word + pyg
        print new_word
    else:
        new_word = word[1:] + first + pyg
        print new_word

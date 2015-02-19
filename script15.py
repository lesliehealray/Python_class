# loops

count = 0

while True:
    print count,
    # can be written as count = count + 1
    count += 1
    if count > 10:
        break

choice = raw_input('Are you hungry? (y/n)').lower()
valid = ['y', 'n']

# dealing with  bad input
while choice not in valid:
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

answer = 23
question = 'What number am i thinking of? '
print "Let's play the guessing game!"

while True:
    guess = int(raw_input(question))
    if guess < answer:
        print ('Little higher')
    elif guess > answer:
        print ('Little lower')
    else:
        print 'you a mind reader!'.upper()

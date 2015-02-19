print 'You enter a dark room with two doors. Do you go through door # or door #2?'
door = raw_input('enter 1 or 2: ')
if door == '1':
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear"
    bear = raw_input("Enter 1 or 2: ")
    if bear == "1":
        print "The bear eats your legs off. Good job!"
    if bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "You didn't %s . Bear runs away." % bear
elif door == '2':
    print 'You stare into the endless abyss at Cthulhu\'s retina. What do you see?'
    print '1. Blueberries.'
    print '2. Yellow jacket clothespins.'
    print '3. Understanding revolvers yelling melodies.'
    insanity = raw_input('Enter 1, 2, or 3  ')
    if insanity == '1' or insanity == '2':
        print 'Your body survives powered by a mind of jello. Good job!'
    else:
        print 'The insanity rots your eyes into a pool of muck. Good Job!'
else:
    print 'You stumble around and fall on a knife and ide. Good job!'

# Write your own adventure story using sudo code first, then real code.

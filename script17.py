total = 0.0

print 'This program will take several numbers, then average them.'
count = int(raw_input('How many numbers would you like to sum:  '))
current_count = 0

while current_count < count:
    print 'Number', current_count
    number = float(raw_input('Enter a number:  '))
    total += number
    current_count += 1

print 'The average was: ', total/count

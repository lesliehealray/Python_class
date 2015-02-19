pi = 3.14
print type(pi)
print str(pi)
text = 'The value of pi is %d' % pi
print text
text = 'The value of pi is %r' % pi
print text
#below comment will fail
#text = 'The value of pi is ' + pi
text = 'The value of pi is ' + str(pi)
print text

input_value = raw-input("Enter a radius: ")
radius = float(input_value)
area = 3.14159 * radius **2
print 'The area of a circle with radius is %r' % area


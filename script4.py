cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#Below will work
print 'there are', cars, 'cars available.'
print 'There are only', cars, 'cars'
print 'There are only', drivers, 'drivers availabe.'

#Below is better. Why? Rewrite the above code using substitution
print 'There will be %d emtpy cars today' % cars_not_driven
print 'We can transport %s people today' % carpool_capacity
print 'We have %s to carpool today' % passengers
print 'We need to put about %d in each car' %average_passengers_per_car
#%d and %s work . %s  usually reserved for strings and %d reserved for numbers.

#another way substitution using strings
text = '%d little pigs come out or I\'ll %s and %s and %s your house down.' % (3, 'huff', 'puff', 'blow')
print text

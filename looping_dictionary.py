phone_book = {
    'Leslie': 8981234567,
    'David': 9194325678,
    'Caleb': 9191232222,
    'Sylvia': 9192323222
}

for name in phone_book:
    print name

for name, number in phone_book.iteritems():
    print 'Phone number of %s is %d' % (name, number)
    print 'Phone number of {} is {}'.format(name, number)

age = raw_input("Enter your age: ")


if age <= 10:
    print 'You are a kid.'
elif age > 10 and age <= 19:
    print 'You are a teenager.'
elif 20 <= age <= 64:
    print 'You are an adult.'
else:
    print 'You are a wizard.'

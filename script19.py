# Functions
# The difference between and return.


def function_that_prints():
    print 'I printed'


def function_that_returns():
    return 'I returned'


f1 = function_that_prints()
f2 = function_that_returns()
print 'Now let us see what the values of f1 and f2 are'
print f1
print f2

# print just shows the human user  a string representing what is going on inside the computer.
# print will not in any way affect a function.
# print Can be useful for debugging or for checking various values in a program without disrupting it.
# return is the main way a function gives back a value. This value is often unseen by the human user.
# all functions returns a value and will return none if there is no return statement.
# Return values can be used further in other functions.

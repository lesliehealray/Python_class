#! /usr/bin/python
# shebang  #! (says run me as a script in the interpreter)
#  specified  by the  rest of the first line in the file
# if you want to run your file as an executable.

n = raw_input('Pick an integer: ')
n = int(n)
if n < 0:
    print 'The absolute value of %d is %d' % (n, abs(n))
else:
    print 'The absolute value of %d is %d' % (n, n)

# intro to conditional expression if/else

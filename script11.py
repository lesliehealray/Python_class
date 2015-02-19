# A list is an ordered set. It can be concatenated with the + operator.
# https://docs.python.org/2.7/library/stdtypes.html?highlight=list%20methods
# The first element of any list is index zero

my_list = ['a', 'b', 'c']
# finds the first occurrence of a value in the list nad returns the index. I
# if the value isn't found, Python raises an objection
print my_list.index('a')

# slicing
print my_list[1:3]
my_list.extend(['d', 'e', 'f'])
print my_list
new_list = ['go', 'leave', 'stay']
weird_list = new_list + my_list
print weird_list
fun_list = my_list * 3
print fun_list
# first occurrence of a value in the list and returns the index
my_list.index('a')
# removes the first occurence. Doesn't return a value
my_list.remove('a')
print my_list
# removes the last element of the list andreturns the value that it removed.
# doesn't take an argument. Explain argument.
print my_list.pop()

# using the above and reading more in the docs, create/modify your own list.

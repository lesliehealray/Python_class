# # unordered key value pairs

# phonebook = {
#     'John' : 9199621000,
#     'Jack' : 9192341000,
#     'Jill' : 7873454444
# }
# print phonebook

# my_phonebook = {}

# my_phonebook['John'] = 9199621000
# my_phonebook['Jack'] = 9192341000
# my_phonebook['Leslie'] = 9192345678

# print my_phonebook

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
phonebook["Jake"] = 938273443
del phonebook["Jill"]
# or in lieu of above, use .pop method
# phonebook.pop("John")
# testing code
if "Jake" in phonebook:
    print "Jake is listed in the phonebook."
if "Jill" not in phonebook:
    print "Jill is not listed in the phonebook."

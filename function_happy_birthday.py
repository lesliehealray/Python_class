def happy_birthday(name):
    return '\nhappy birthday to you \n\
happy birthday to you \n\
happy birthday dear {}\n\
happy birthday to you'.format(name)

# print happy_birthday('david')
# print happy_birthday('Sylvia')
# print happy_birthday('Rebecca')
# print happy_birthday('Leslie')
kittens = raw_input('what is your cats name?  ')
print happy_birthday(kittens)

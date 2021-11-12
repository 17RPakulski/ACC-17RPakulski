user = input('Enter: ')

for word in user:
    if word == ' ':
        user.replace(' ', '-')
        print(word)
        
    else:
        print(word)
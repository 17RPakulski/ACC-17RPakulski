user = input('Enter: ')
word = ''

for i in user:
    if i == '-':
        print(word)
        word = ''
    else:
        word = word + i
        
    
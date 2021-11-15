user = input('Enter: ')
print()
length_of_user = len(user)
counter = 0
consonant = 0

while counter < length_of_user:
    ch = user[counter]
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print(ch)
    else:
        consonant = consonant + 1
    
    counter = counter + 1
print(consonant)
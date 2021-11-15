user = input('Enter: ')
print()
length_of_user = len(user)
counter = 0

while counter < length_of_user:
    ch = user[counter]
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print(ch)
    
    counter = counter + 1


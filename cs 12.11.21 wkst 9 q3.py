# Variable

default_list = ['a', 'b', 'c', 'd']

# Menu

print('''
1. Append an element
2. Insert an element
3. Append a list to the given list
4. Modify an existing element
5. Delete an existing element from its position
6. Delete an existing element with a given value
7. Sort the list in the ascending order
8. Sort the list in descending order
9. Display the list. 
''')


############################################################################
user = int(input('Enter Your Choice From 1-9: '))

if user < 0 or user > 10:
    print('Error...')
    
elif user == 1:
    print('###############################################################')
    print('List before operation' + default_list)
    
    list.append(
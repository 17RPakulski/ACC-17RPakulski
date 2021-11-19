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


user = int(input('Enter Your Choice From 1-9: '))
print()

if user < 0 or user > 9:
    print('Error')
    
elif user == 1:
    print('*******************************************')
    print('Option 1: Append an Element')
    print('*******************************************')
    print()
    
    
    user_append = input('Enter the element to be Appended to the List: ')
    print('List before operation:' , default_list)
    default_list.append(user_append)
    print('List after operation: ' , default_list)
    


elif user == 2:
    print('*******************************************')
    print('Option 2: Insert an Element')
    print('*******************************************')
    print()
    
    
    user_location = int(input('Enter the place you want to insert(using a digit): '))
    if user_location < 1 or user_location > len(default_list):
        print('invalid digit')
        exit()
    
    user_insert = input('Enter the element you want to insert: ')
    
    print('List before operation:' , default_list)
    
    list = default_list
    list.insert(user_location - 1, user_insert)
    
    print('List after operation: ' , list)
    
    
'''

This is annoyin me



# list.append(x) #appends x to the end of the list
elif user == 3:
    user_list_str = input('Enter Elements: ')

    
    
    for character in user_list_str:
        if character == ',':
        
        

I dont understand what you mean by modify
elif user == 4:
    
'''

#change this if to an elif(when i did elif i got error)
if user == 5:
    user_position = input('Enter the name of item to delete: ') 
    default_list.remove(user_position)
    print(default_list)
    

'''
    print('List before operation:' , default_list)
    list = default_list
    list.insert(user_location - 1, user_insert)
    
    print('List after operation: ' , list)
'''

# i done know what choice 6 means











    
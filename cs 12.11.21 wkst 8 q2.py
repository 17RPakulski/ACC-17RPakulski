add = 0
user = input('Enter: ')
print()

for num in user:
    if num.isdigit():
        num = int(num)
        add = (add + num)
       
print(add)

        
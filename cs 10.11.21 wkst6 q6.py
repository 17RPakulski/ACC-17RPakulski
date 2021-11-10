#outer loop
user = int(input('enter: ')) + 1

for i in range(user):
    for j in range(i):
        print('*', end=' ')
    print()
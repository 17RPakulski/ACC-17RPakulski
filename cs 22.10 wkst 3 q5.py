
num1 = int(input('Enter First Number: '))
num2 = int(input('Enter Second Number: '))

if num1 > num2:
    largeNum = num1
    smallNum = num2
else:
    largeNum = num2
    smallNum = num1

mod = 1

while mod > 0:
    mod = (largeNum % smallNum)
    largeNum = smallNum
    smallNum = mod
    print(mod)
    

    
    

    
    
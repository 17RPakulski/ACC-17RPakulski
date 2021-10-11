#i put all the programs into one file, i hope thats not a problem:)


# Q1
num1 = input('First Number: ')
num2 = input('Second Number: ')

numbers = [num1, num2]
print(int(max(numbers)))
print(int(min(numbers)))

# Q2
age = int(input('Your age: '))

if age < 18:
    print('This person is not eligible for voting')
else:
    print('This person is eligible for voting')

# Q3
num = int(input('Write a number: '))
if num % 2 == 0:
    print('Even')
else:
    print('Odd')

# Q4
number = int(input('Write a number: '))

if number % 7 == 0:
    print('This number is divisible by 7')
else:
    print('This number is not divisible by 7')

# Q5
numberr = int(input('Write a number: '))
if numberr % 5 == 0:
    print('Hello')
else:
    print('Bye')

# Q6
unit = int(input('Unit: '))
if unit <= 100:
    print('no charge')
elif unit > 100 and unit < 200:
    print(unit * 0.05)
elif unit > 200:
    print(unit * 0.10)
#I dont know wha to do for question 6 to be honest :(

# Q7
lastdigit = int(input('Write a number: '))
print(lastdigit % 10)

# Q8
divide3 = int(input('Write a number: '))
if divide3 % 3 == 0:
    print('Is divisible')
else:
    print('not divivible')

# Q9

num17 = int(input('Write a number between 1 - 7: '))

if num17 == 1:
    print('Sunday')
elif num17 == 2:
    print('Monday')
elif num17 == 3:
    print('Tueday')
elif num17 == 4:
    print('Wednesday')
elif num17 == 5:
    print('Thursday')
elif num17 == 6:
    print('Friday')
elif num17 == 7:
    print('Saturday')
else:
    print('This is not a number between 1-7')

# Q10
temp= float(input('Write celsius: '))
print(temp * 1.8 + 32)

# Q 1
# Not too sure what to do for Q1 page 3




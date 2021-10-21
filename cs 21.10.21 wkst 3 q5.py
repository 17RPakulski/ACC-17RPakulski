counter = 0
gcd = 0
#GCD (m,n)= GCD (n, m mod n)
num1 = int(input('Enter First Number: '))
num2 = int(input('Enter Second Number: '))
while counter < 1:
    counter = counter + 1
    divide = num1 / num2
    remainder = num1 % num2
    gcd = num2 * divide + remainder

print(gcd)
    
    
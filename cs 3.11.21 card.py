number = int(input('Enter a Number: '))
odddigit = 0
evendigit = 0

while number > 0:
    odddigit = odddigit + number % 10
    number = number // 10
    evennumber = number % 10 * 2
    if evennumber > 9:
        while evennumber > 0:
            evendigit = evendigit + evennumber % 10
            evennumber = evennumber // 10
    else:
        evendigit = evendigit + evennumber
       
    number = number // 10
    
total = odddigit + evendigit

if total % 10 == 0:
    print('valid')
else:
    print('not valid')
    
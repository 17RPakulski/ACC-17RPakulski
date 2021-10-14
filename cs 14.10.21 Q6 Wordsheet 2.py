unit = int(input('Enter units: '))

cent5 = 0
cent10 = 0

if unit <= 100:
    print('no charge')

elif unit < 200:
    cent5 = ((unit - 100) * 5)
    print(cent5)
    
else:
    cent10 = ((unit - 200) * 10 + 500)
    print(cent10)
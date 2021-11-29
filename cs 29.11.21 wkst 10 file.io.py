# Open Files
'''
Home computer directories:
file10 = open('C:/Users/rober/Downloads/10Random.txt', 'r')
file100 = open('C:/Users/rober/Downloads/100Random.txt', 'r')
'''

file10 = open('C:/Users/17RPakulski.ACC/Downloads/10Random (2).txt', 'r')
file100 = open('C:/Users/17RPakulski.ACC/Downloads/100Random (2).txt', 'r')

#vVariables
min_num = 99999999999999999999999999999999999999999999999999999
max_num = 0


# 10 Random
print('############################# 10 RANDOM #############################')

# Range
for line in file10:
    print(line)
    for item in line.split():
        number = int(item)
        
        if(number < min_num):
            min_num = int(item)

        if(number > max_num):
            max_num = int(item)


rangee = max_num - min_num
print('--- Range =', rangee)
print()

file10.close()


# Frequency      GO BACK TO THIS AND DONT PRINT SAME NUMBER FREQUENCY TWICE
file10 = open('C:/Users/17RPakulski.ACC/Downloads/10Random (2).txt', 'r')

frequency = []


for line in file10:
    for item in line.split():
        count = line.count(item)
        frequency.append(count)

print(line.split())
print('--- Frequency =', frequency)
print()
file10.close()

# Mean

file10 = open('C:/Users/17RPakulski.ACC/Downloads/10Random (2).txt', 'r')
add = 0
numbers = 0

for line in file10:
    for item in line.split():
        add = (add + int(item))
        numbers = numbers + 1

mean = (add / numbers)        
print('--- Mean =', mean)
print()

file10.close()
# Median

file10 = open('C:/Users/17RPakulski.ACC/Downloads/10Random (2).txt', 'r')
l = []
add_two_mid = 0

for line in file10:
        for item in line.split():
            l.append(item)
            l.sort()
            
len_list = len(l)
half_len = len_list // 2
''' Not too sure wha
if half_len % 2 != 0:
    half_len_minus = half_len - 1
    half_len_plus = half_len + 1
    add_two_mid = (l[int(half_len_minus)] + l[int(half_len_plus)]) / 2
    print('--- Median =', add_two_mid)
'''
#else: should be else but the code above is not working 
index_median = l[half_len]
print('--- Median =', index_median)
file10.close()

# Mode

file10 = open('C:/Users/17RPakulski.ACC/Downloads/10Random (2).txt', 'r')
mode = 0
item_count = 0

for line in file10:
    for item in line.split():
        item_count = item.count(item)
        if item_count > mode:
            mode = item

print('--- Mode =', mode)

    
        




















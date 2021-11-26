# Open Files
file10 = open('C:/Users/17RPakulski.ACC/Downloads/10Random.txt', 'r')
file100 = open('C:/Users/17RPakulski.ACC/Downloads/100Random.txt', 'r')

#vVariables
min_num = 99999999999999999999999999999999999999999999999999999
max_num = 0

# 10 Random
print('############################# 10 RANDOM #############################')
for line in file10:
    print(line)
    for item in line.split():
        number = int(item)
        
        if(number < min_num):
            min_num = int(item)

        if(number > max_num):
            max_num = int(item)


rangee = max_num - min_num
print('Range =', rangee)


# Frequency

for line in file10:
    list(line)
    print(line)

    





























'''
# 100 Random
print('############################# 100 RANDOM #############################')
for line in file100:
    print(line)
'''
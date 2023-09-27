dict = {2:6,1:3, 9:2,4:3,3:1}
def histogram(dict):
    for key,value in dict.items():
        print(f'{key}| {"=" * value * 3} {value}')

histogram(dict)

# OR

data = [2,2,2,2,1,1,1,2,9,9,4,4,4,3]
frequency = {}

for value in data:
    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1

    
for key, value in frequency.items():
    print(f'{key}| {"=" * value * 3} {value}')
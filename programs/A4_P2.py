dict = {2:4, 1:6, 9:1, 7:3}
default_design = '=== '
user_design = str(input("Enter the desired design: "))

for key,value in dict.items():
    max_value = None
    max_key = None
    if max_value == None or value > max_value:
        max_value = value
        max_key = key
print(max_value)


for key in dict.items():
    if len(key) > max_key:
        max_key = len(key)


align = ' ' * max_key

def histogram(dict, design,):
    
    for key,value in dict.items():
        print(f'{key}| {design * value} {value} {align}')

if user_design:
    histogram(dict,user_design)
else:
    histogram(dict,default_design)
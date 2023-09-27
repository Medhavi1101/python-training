min_range = int(input("Enter the min range: "))
max_range = int(input("Enter the max range: "))

for x in range(min_range,max_range+1):
    if x > 1:
        for i in range(2, x):
            if(x % i) == 0:
                break
        else:
            print(x)
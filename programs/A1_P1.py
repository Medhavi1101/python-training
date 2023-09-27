lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is:", max(lst))


x = int(input("Enter no. of inputs: "))
count = 0
while count < x:
    number = int(input('Enter number: '))
    if largest==None:
        largest=number
    elif number > largest:
        largest = number
    count +=1
print("the largest number is:", largest)


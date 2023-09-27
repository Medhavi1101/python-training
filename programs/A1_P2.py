n = int(input("How many numbers you want to enter? "))
if n > 1:
    largest = int(input())  
    secLargest = int(input())  
    if secLargest > largest:
        t = secLargest
        secLargest = largest
        largest = t
    for i in range(n - 2):
        a = int(input())
        if a > largest:
            secLargest = largest
            largest = a
        elif a > secLargest:
            secLargest = a
    print("Second Largest Number =", secLargest)
else:
    print("Please enter more than 1 number")



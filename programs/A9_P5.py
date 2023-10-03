def bubble_sort(input_list):
    n = len(input_list)

    for i in range(n):
        for j in range(n-i-1):
            if(input_list[j]) > input_list[j+1]:
                input_list[j], input_list[j+1]  = input_list[j+1], input_list[j]

    return input_list

list = [3,2,5,9,1,6]
sorted_list = bubble_sort(list)
print(sorted_list)
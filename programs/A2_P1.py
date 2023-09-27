def freq(sequence):
    dict = {}

    for value in sequence:
        if value in dict:
            dict[value] += 1
        else:
            dict[value] = 1
    return dict
    
values = [ 2,2,9,1,2,2,1,4,2,2,3,1]
output = freq(values)
    
for key, value in output.items(): 
    print(f"{key}: {value}")
        
    
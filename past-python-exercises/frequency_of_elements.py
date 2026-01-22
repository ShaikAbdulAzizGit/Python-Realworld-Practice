def frequency_of_elements(list):
    frequency_map={}
    for l in list:
        if l in frequency_map:
            frequency_map[l]+=1
        else:
            frequency_map[l]=1
    return frequency_map

numbers=[4,2,6,3,1,7,4,2,5,9,4,2,6,3,2,7,4]

result=frequency_of_elements(numbers)
print(result)
def find_highest_frequency_number(numbers):
    frequecy_map={}
    for num in numbers:
        if num in frequecy_map:
            frequecy_map[num]+=1
        else:
            frequecy_map[num]=1
    most_frequent_value=max(frequecy_map,key=frequecy_map.get)
    return most_frequent_value,frequecy_map[most_frequent_value]

numbers = [2, 4, 5, 2, 3, 2, 4, 4, 4, 5]

most_frequent_value,most_frequent_value_frequency=find_highest_frequency_number(numbers)
print(f"Most frequent number is {most_frequent_value}, appearing {most_frequent_value_frequency} times.")
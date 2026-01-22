def second_largest_frequent_number_finder(numbers):
    frequency_map={}
    for num in numbers:
        if num in frequency_map:
            frequency_map[num]+=1
        else:
            frequency_map[num]=1
    sorted_items=sorted(frequency_map.items(),key=lambda x:x[1],reverse=True)
    if len(sorted_items)>=2:
        second_most_value=sorted_items[1][0]
        second_most_frequency=sorted_items[1][1]
        return second_most_value,second_most_frequency
    else:
        return None,0
    



numbers = [1,1,1,1,1,1,1, 2, 2, 3, 3, 3,4,4,4,4,4,4,4,4,4, 4, 4, 4]
second_most_value,second_most_frequency=second_largest_frequent_number_finder(numbers)
print(f"The second most frequent value is {second_most_value} apperaing {second_most_frequency} times")
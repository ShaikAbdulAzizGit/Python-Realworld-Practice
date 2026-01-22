def remove_duplicates(numbers):
    seen=set()
    new_list=[]
    for num in numbers:
        if num not in seen:
            seen.add(num)
            new_list.append(num)
    return new_list



numbers=[4, 2, 5, 2, 3, 4, 6, 2]
result=remove_duplicates(numbers)
print(result)
def remove_duplicates(list1,list2):
    common_values=[]
    for val in list1:
        if val in list2 and val not in common_values:
            common_values.append(val)
    return common_values

list1 = [1, 2, 2, 3, 4, 5,5,5,5,5,5,5,5]
list2 = [3, 4, 4, 5, 6, 7]

print(remove_duplicates(list1,list2))
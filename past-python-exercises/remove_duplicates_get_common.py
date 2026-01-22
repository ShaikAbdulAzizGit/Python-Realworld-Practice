def remove_duplicates(numbers):
    new_list=[]
    for num in numbers:
        if num not in new_list:
            new_list.append(num)

    return new_list

def get_common_values(l1,l2):
    common_values=[]
    for l in l1:
        if l in l2:
            common_values.append(l)
    return common_values


def main(l1,l2):
    common_values=get_common_values(l1,l2)
    return remove_duplicates(common_values)



list1 = [1, 2, 2, 3, 4, 5, 5]
list2 = [3, 4, 4, 5, 6, 7]

print(main(list1,list2))
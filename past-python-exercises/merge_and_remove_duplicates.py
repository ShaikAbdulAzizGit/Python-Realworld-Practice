def remove_duplicates(numbers):
    seen=set()
    new_list=[]
    for num in numbers:
        if num not in seen:
            seen.add(num)
            new_list.append(num)
    return new_list

def merge_list(list1,list2):
    return list1+list2

def main(list1,list2):
    res=remove_duplicates(merge_list(list1,list2))
    return res

def merge_and_remove_duplicates(l1,l2):
    return list(set(l1+l2))


list1 = [1, 2, 2, 3, 4]
list2 = [3, 4, 4, 5, 6]

result=main(list1,list2)
print(result)
print(merge_and_remove_duplicates(list1,list2))
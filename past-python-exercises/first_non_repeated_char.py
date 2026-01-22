def first_non_repeated_char(sample_string):
    frequency_map={}
    for s in sample_string:
        if s in frequency_map:
            frequency_map[s]+=1
        else:
            frequency_map[s]=1
    non_repeated_char=sorted(frequency_map.items(),key=lambda x:x[1])[0][0]
    return f'First non-repeated character is: {non_repeated_char}'



sentence = "aabbcdddeeffgghhiijjkklmn"
print(first_non_repeated_char(sentence))





# ChatGpt
# def first_non_repeated_char(sample_string):
#     frequency_map = {}
    
#     # Count frequency
#     for char in sample_string:
#         frequency_map[char] = frequency_map.get(char, 0) + 1

#     # Find the first non-repeated character in original order
#     for char in sample_string:
#         if frequency_map[char] == 1:
#             return f'First non-repeated character is: {char}'
    
#     return "No non-repeated character found"
    

# sentence = "aabbcdddeeffgghhiijjkklmn"
# print(first_non_repeated_char(sentence))

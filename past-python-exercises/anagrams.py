# def check_anagrams(str1,str2):
#     if sorted(str1) == sorted(str2):
#         return True
#     else:
#         return False
    



# s1='silent'
# s2='listen'

# print(check_anagrams(s1,s2))


def check_frequency(sample_string):
    frequency_map={}
    for s in sample_string:
        if s in frequency_map:
            frequency_map[s]+=1
        else:
            frequency_map[s]=1

    return frequency_map
def compare_frequencies(str1,str2):
    if check_frequency(str1)==check_frequency(str2):
        return True


str1='silent'
str2='listen'
if compare_frequencies(str1,str2):
    print("The both strings are anagrams")
else:
    print("The both strings are not anagrams")







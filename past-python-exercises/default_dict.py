from collections import defaultdict

def return_one():
    return 1
dict=defaultdict(return_one) #Empty dictionary assigns 1 as default value
dict['apple']+=1 #Throws error if we are using normal dictionary

print(dict)




# map() Tasks

# Task 1

prices = [1000, 2500, 3000]

res=list(map(lambda x:x/100 if x>=1000 else 0,prices))

print(res)


# Task 2

emails = ["ALI@GMAIL.COM", "Sara@Yahoo.Com", "john@outlook.com"]

res = list(map(lambda x:x.strip().lower(),emails))

print(res)

# Task 3

users = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"},
    {"id": 3, "name": "John"}
]
res=list(map(lambda x:x['name'],users))

print(res)

# Task 4

prices = [500, 1000, 1500]

res=list(map(lambda x:x*0.10,prices))

print(res)


# Task 5

values = ["10", "20", "30"]

res=list(map(lambda x:int(x),values))

print(res)


# filter() Tasks

# Task 1

def is_valid(age):
    if age>0:
        return True
    else:
        return False

ages = [22, 17, -3, 45, 0, 30]

res=list(filter(is_valid,ages))

print(res)


# Task 2

def is_active(user):
    if user['active']:
        return True
    else:
        return False
    

users = [
    {"name": "Ali", "active": True},
    {"name": "Sara", "active": False},
    {"name": "John", "active": True}
]

res=list(filter(is_active,users))

print(res)

# Task 3

def is_valid_string(string):
    string=string.strip()
    if string:
        return True
    else:
        return False

data = ["Ali", "", "Sara", "  ", "John"]

res=list(filter(is_valid_string,data))

print(res)

# Task 4

prices = [700, 1200, 300, 2500]

res=list(filter(lambda x:True if x>1000 else False,prices))

print(res)


# Task 5

emails = ["a@gmail.com", "invalid", "b@yahoo.com"]

res=list(filter(lambda x:True if '@' in x else False,emails))

print(res)


# reduce() Tasks

from functools import reduce

# Task 1

orders = [250, 500, 750]

res=reduce(lambda x,y:x+y,orders)

print(res)


# Task 2

scores = [65, 78, 90, 88]

res=reduce(lambda x,y:x if x>y else y,scores)

print(res)

# Task 3

factors = [2, 3, 4]

res=reduce(lambda x,y:x*y , factors)

print(res)


# Task 5

files = ["a.txt", "report.pdf", "long_filename_data.csv"]

res=reduce(lambda x,y:x if len(x)>len(y) else y,files)

print(res)







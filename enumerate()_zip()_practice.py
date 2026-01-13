# enumerate() Tasks

# Task 1

ages = [22, 17, -3, 45, 0, 30]

for index,age in enumerate(ages):
    if age<=0:
        print(index,age)


# Task 2
readings = [23.5, 24.0, None, 25.1, None, 26.3]

filtered_indexes=[index for index,Value in enumerate(readings) if Value==None]

print(filtered_indexes)


# Task 3


prices = [1000, 2500, 3000]

prices=[price/100 for price in prices]

print(prices)


# Task 4

logs = ["Server started", "DB connected", "Request received"]

for index,log in enumerate(logs,start=1):
    print(f"{index}. {log}")


# Task 5

transactions = [120, 450, 980, 1500, 300]

for index,value in enumerate(transactions):
    if value>1000:
        print(index,value)
        break


# zip() Tasks 

# Task 1

fields = ["name", "email", "age"]
values = ["Ali", "ali@gmail.com", 22]

res={}

res=dict(zip(fields,values))

print(res)


# Task 2

features = [2.5, 3.0, 4.1]
labels = [0, 1, 1]

for feature,label in zip(features,labels):
    print(feature,label)


# Task 3

products = ["Laptop", "Mouse", "Keyboard"]
prices = [70000, 500, 2000]

for product,price in zip(products,prices):
    if price>1000:
        print(product)


# Task 4

user_ids = [101, 102, 103, 104]
login_status = [True, False, True]

if len(user_ids) != len(login_status):
    print("WARNING : Be careful the above two lists are not of same length ")

for id,status in zip(user_ids,login_status):

    print(id,status)


# Task 5

students = ["Ali", "Sara", "John"]
marks = [35, 80, 60]

for index,(student,mark) in enumerate(zip(students,marks),start=1):
    if mark<40:
        print(f'{index} . {student} : Fail')
    else:
        print(f'{index} . {student} : Pass')


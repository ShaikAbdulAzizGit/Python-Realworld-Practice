# Task 1

users = [
    {"id": 1, "name": "Ali", "age": 22, "is_active": True},
    {"id": 2, "name": "Sara", "age": 17, "is_active": False},
    {"id": 3, "name": "John", "age": 25, "is_active": True},
    {"id": 4, "name": "Aisha", "age": 30, "is_active": False},
    {"id": 5, "name": "Rahul", "age": 19, "is_active": True}
]

total_users=len(users)
active_users=0
adult_users=0
inactive_users=[]
total_age=0

print(total_users)

for user in users:
    if user['is_active']:
        active_users+=1
    else:
        inactive_users.append(user['name'])

    if user['age']>=18:
        adult_users+=1

    total_age+=user['age']

average_age=total_age/total_users

print(
    f"Total users: {total_users}",
    f"Active users: {active_users}",
    f"Adults: {adult_users}",
    f"Inactive users: {inactive_users}",
    f"Average age: {average_age}",
    sep='\n'
)


# Task 2

inventory = {
    "apple": {"price": 50, "quantity": 20},
    "banana": {"price": 10, "quantity": 0},
    "orange": {"price": 30, "quantity": 15},
    "mango": {"price": 100, "quantity": 5}
}

total_inventory_value=0
out_of_stock_products=[]
most_expensive_product=""
product_with_highest_quantity=""
product_morethan_500=[]
most_expensive_price=0
highest_quantity=0

for key,value in inventory.items():
    total_inventory_value+=(value['price']*value['quantity'])

    if value['quantity']==0:
        out_of_stock_products.append(key)

    if value['price']*value['quantity'] > 500 :
        product_morethan_500.append(key)

    if value["price"]>most_expensive_price:
        most_expensive_price=value["price"]
        most_expensive_product=key

    if value["quantity"] > highest_quantity:
        highest_quantity=value["quantity"]
        product_with_highest_quantity=key

print(f"Higest price: {most_expensive_price}")
print(f"Higest quantity: {highest_quantity}")
print(f"Total Inventory value : {total_inventory_value}")
print(f"Out of stock products : {out_of_stock_products}")
print(f"most Expensive prouct : {most_expensive_product}")
print(f"Product with highest quantity : {product_with_highest_quantity}")
print(f"Products list worth more than 500 : {product_morethan_500}")


# Task 3

orders = [
    "apple", "banana", "apple", "orange", "banana",
    "apple", "mango", "banana", "banana", "orange"
]

frequency_map={}
highest_frequency=0
most_ordered_item=""
items_ordered_once=[]

for order in orders :
    if order in frequency_map:
        frequency_map[order]+=1
    else:
        frequency_map[order]=1

for item , frequency in frequency_map.items():
    if frequency > highest_frequency:
        highest_frequency=frequency
        most_ordered_item=item

    if frequency == 1 :
        items_ordered_once.append(item)

print(f"Most ordered Item : {most_ordered_item}")
print(f"Items ordered only once : {items_ordered_once}")


# Task 4

students = {
    "Ali": [78, 85, 90],
    "Sara": [88, 92, 79],
    "John": [60, 65, 70],
    "Aisha": [95, 98, 100]
}

average_map={}
max_average=0
top_scoring_student=""
students_with_low_average=[]

for student , marks in students.items():
    total_subjects=len(marks)
    total_marks=0

    for mark in marks:
        total_marks+=mark

    average=total_marks/total_subjects
    average_map[student]=average

    if max_average<average:
        max_average=average
        top_scoring_student=student

    if average < 75 :
        students_with_low_average.append(student)

print(average_map)
print(f"Top scoring student : {top_scoring_student}")
print(f"students average less than 75 : {students_with_low_average}")


# Task 5

emails_source_1 = ["a@gmail.com", "b@gmail.com", "c@gmail.com", "d@gmail.com"]
emails_source_2 = ["c@gmail.com", "d@gmail.com", "e@gmail.com"]

emails_source_1=set(emails_source_1)
emails_source_2=set(emails_source_2)

common_emails=emails_source_1.intersection(emails_source_2)
unique_emails=emails_source_1.symmetric_difference(emails_source_2)

print(f"Common Emails : {common_emails}")
print(f"Unique emails : {unique_emails}")

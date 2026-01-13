# Task 1

users = [
    {"id": 1, "name": "Ali", "is_active": True, "role": "admin"},
    {"id": 2, "name": "Sara", "is_active": False, "role": "user"},
    {"id": 3, "name": "John", "is_active": True, "role": "user"},
    {"id": 4, "name": "Aisha", "is_active": True, "role": "admin"},
]

active_admins=[user["name"] for user in users if user['is_active'] and user['role']=='admin']


# Task 2

numbers = [120, 45, 67, 89, 150, 30, 200]


labels=['HIGH' if n >= 100 else 'LOW' for n in numbers]

print(labels)

# Task 3

orders = [
    {"order_id": 1, "items": ["apple", "banana"]},
    {"order_id": 2, "items": ["milk"]},
    {"order_id": 3, "items": ["bread", "butter", "jam"]},
]


all_items=[item for order in orders for item in order['items']]

print(all_items)


# Task 4

def get_average(marks):
    sum=0
    for mark in marks:
        sum+=mark
    average=sum/len(marks)
    return round(average,2)
    
students = {
    "Ali": [78, 85, 90],
    "Sara": [88, 92, 79],
    "John": [60, 65, 70],
}


students_average={name:get_average(marks) for name,marks in students.items()}

print(students_average)


# Task 5

logs = [
    "INFO: User logged in",
    "ERROR: Invalid password",
    "",
    "WARNING: Disk space low",
    "ERROR: Timeout",
    "INFO: User logged out"
]

error_messages=[message.split(':')[1] for message in logs if message!="" and message.startswith('ERROR')]


print(error_messages)




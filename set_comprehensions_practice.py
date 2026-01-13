# Task 1


name='Hello'

emails = [
    "ali@gmail.com",
    "SARA@gmail.com",
    "john@yahoo.com",
    "ali@gmail.com",
    " sara@gmail.com ",
    "",
    "JOHN@yahoo.com"
]


result={email.strip().lower() for email in emails if email.strip()}

print(result)


# Task 2

blocked_users = [101, 102, 103, 101, 104, 102]



result={user for user in blocked_users}

print(result)



# Task 3

orders = [
    {"order_id": 1, "items": ["apple", "banana", "apple"]},
    {"order_id": 2, "items": ["milk", "banana"]},
    {"order_id": 3, "items": ["bread", "butter", "milk"]},
]



result={item for order in orders for item in order['items']}

print(result)



# Task 4


values = [10, 15, 20, 10, -5, 0, 15, -5, 30]


result={value for value in values if value >0}

print(result)



# Task 5

logs = [
    "ERROR: Disk full",
    "WARNING: CPU high",
    "ERROR: Disk full",
    "INFO: System rebooted",
    "ERROR: Network down"
]


result={message.split(':')[1].strip() for message in logs if message.startswith('ERROR')}

print(result)


# List methods

# Task 1

records = [
    {"id": 1, "valid": True},
    {"id": 2, "valid": False},
    {"id": 3, "valid": True},
    {"id": 4, "valid": False}
]

valid_records=[]
invalid_records=[]

for record in records:
    if record['valid']:
        valid_records.append(record)
    else:
        invalid_records.append(record)

print(valid_records)
print(invalid_records)


# Task 2

page1 = [1, 2, 3]
page2 = [4, 5]
page3 = [6, 7, 8]

final_output=[]
final_output.extend(page1)
final_output.extend(page2)
final_output.extend(page3)

print(final_output)


# Task 3

jobs = ["job1", "job2", "job3"]

while jobs:
    print(jobs.pop(0))

# Task 4

blocked_users = [101, 102, 103, 104]
user_to_remove = 103


if user_to_remove in blocked_users:
    blocked_users.remove(user_to_remove)
    print(blocked_users,' Removed successfully')

print(blocked_users)


# Task 5

logs = [
    {"id": 1, "timestamp": 170},
    {"id": 2, "timestamp": 120},
    {"id": 3, "timestamp": 200}
]


logs.sort(key=lambda log:log['timestamp'],reverse=True )

print(logs)


# Task 6

scores = [88, 72, 95, 60]

sorted_list=sorted(scores,reverse=True)

print(sorted_list)

# Task 7

errors = ["INFO", "WARNING", "CRITICAL", "INFO"]

if errors.count('CRITICAL') > 0:
    print(True)



# Task 8

headers = ["Host", "Content-Type", "Authorization", "Accept"]

print(headers.index("Authorization"))


# Task 9

data = [1, 2, 3, 4, 5, 6 ]

batches=[]
buffer=[]

for item in data:
    buffer.append(item)
    if len(buffer) == 3 :
        batches.append(buffer.copy())
        buffer.clear()

print(batches)


# Task 10

tasks = [
    {"task": "A", "priority": 3},
    {"task": "B", "priority": 1},
    {"task": "C", "priority": 2}
]

tasks.sort(key=lambda t:t['priority'])

print(tasks)

# Task 1

def user_input():
    while True:
        try:
            user_name=input("Enter user name : ")
            password=input("Enter password : ")
            age=int(input("Enter age : "))
            break
        except ValueError:
            print("Unexpected input please try again with valid input ")

    return user_name,password,age


def validate_user():
    all_usernames=[]
    user_name,password,age=user_input()

    if len(user_name)>=4 and len(password)>=8 and age >=18:
        try:
            with open('user_data.txt','r') as f:
                all_lines=f.readlines()

            for line in all_lines:
                all_usernames.append(line.split(',')[0])

            if user_name not in all_usernames:
                with open('user_data.txt','a') as f:
                    f.write(f'{user_name},{age}\n')
                return 'User data successfully saved in file'
            else:
                return f'{user_name} was already added'

        except FileNotFoundError:
            with open('user_data.txt','a') as f:
                f.write(f'{user_name},{age}\n')
            return 'User data successfully saved in file'

    elif len(user_name)<4:
        return 'Username must contain atleast 4 characters'
    elif len(password)<8:
        return 'Passoword must contain alteast 8 characters'
    elif age<18:
        return 'User age must be atleast 18'


status_message=validate_user()
print(status_message)


# Task 2

import json as js

with open('students_unprocessed_data.json','r') as f:
    students_data=js.load(f)

processed_data={}
processed_data['students_data']=[]
processed_data['students_performance_data']=[]

highest_average=0
students_lessthan_75_average=[]

for student in students_data:
    no_of_subjects=len(student['marks'])
    sum_of_marks=0

    for m in student['marks']:
        sum_of_marks+=m

    average=sum_of_marks/no_of_subjects

    if average<75:
        students_lessthan_75_average.append(student['name'])

    if average>highest_average:
        highest_average=average

    processed_data['students_data'].append(
        {'name':student['name'],'average':average}
    )

top_scorer=""

for data in processed_data['students_data']:
    if data['average']==highest_average:
        top_scorer=data['name']

processed_data['students_performance_data'].append(
    {
        'top_scorer':top_scorer,
        'students_average_lessthan_75':students_lessthan_75_average
    }
)

with open('students_data.json','w') as f:
    js.dump(processed_data,f)


# Task 3

orders = [
    {"order_id": 1, "amount": 2500, "status": "completed"},
    {"order_id": 2, "amount": 1500, "status": "pending"},
    {"order_id": 3, "amount": 3200, "status": "completed"},
    {"order_id": 4, "amount": 500, "status": "cancelled"}
]


def get_total_revenue(orders):
    total_revenue=0

    for order in orders:
        total_revenue+=order['amount']

    return total_revenue


def count_order_status(orders):
    completed=0
    pending=0
    cancelled=0

    for order in orders:
        if order['status']=='completed':
            completed+=1
        elif order['status']=='pending':
            pending+=1
        else:
            cancelled+=1

    return completed,pending,cancelled


def get_higest_order(orders):
    order_id=0
    order_value=0

    for order in orders:
        if order['amount']>order_value:
            order_value=order['amount']
            order_id=order['order_id']

    return order_id,order_value


def main(orders):
    total_revenue=get_total_revenue(orders)
    completed,pending,cancelled=count_order_status(orders)
    highest_order_id,highest_order_value=get_higest_order(orders)

    return {
        'total_revenue':total_revenue,
        'total_completed_orders':completed,
        'total_pending_orders':pending,
        'total_cancelled_orders':cancelled,
        'highest_order_id':highest_order_id,
        'highest_order_value':highest_order_value,
    }


print(main(orders))


# Task 4

with open('data.log','r') as f:
    log_data=f.readlines()

info_count=0
error_count=0

for line in log_data:
    if line.startswith("INFO"):
        info_count+=1
    elif line.startswith("ERROR"):
        error_count+=1

with open('log_summary.txt','w') as f:
    f.write(f'Info messages {info_count}\nError messages {error_count}')


# Task 5

with open('input.log','r') as f:
    file_data=f.readlines()

lines_count=len(file_data)
words_count=0
characters_count=0

for line in file_data:
    words_count+=len(line.split(" "))
    for ch in line:
        characters_count+=1

print(f'Lines count : {lines_count}')
print(f'words count : {words_count}')
print(f'characters count : {characters_count}')

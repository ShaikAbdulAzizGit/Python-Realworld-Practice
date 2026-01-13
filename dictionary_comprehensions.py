# Task 1

users = {
    1: {"name": "Ali", "is_active": True},
    2: {"name": "Sara", "is_active": False},
    3: {"name": "John", "is_active": True},
    4: {"name": "Aisha", "is_active": True},
}


active_users={id:data['name'] for id,data in users.items() if data['is_active']}


print(active_users)



# Task 2

scores = {
    "math": 78,
    "physics": 91,
    "chemistry": 65,
    "biology": 88
}


result={subject:'Pass' if marks >=80 else 'Fail' for subject,marks in scores.items()}


print(result)

# Task 3

employees = {
    "Ali": "Backend",
    "Sara": "Frontend",
    "John": "Backend",
    "Aisha": "Data"
}

department_map = {}

for name, department in employees.items():
    department_map.setdefault(department, []).append(name)

print(department_map)

# Task 4

sales = {
    "Jan": 12000,
    "Feb": 18000,
    "Mar": 15000,
    "Apr": 22000
}


result={month:int(sale/1000) for month,sale in sales.items() if sale >=15000}


print(result)


# Task 5

products = {
    "p1": {"name": "Laptop", "price": 70000, "in_stock": True},
    "p2": {"name": "Phone", "price": 40000, "in_stock": False},
    "p3": {"name": "Tablet", "price": 30000, "in_stock": True},
}

result={data['name']:data['price'] for _,data in products.items() if data['in_stock']}

print(result)



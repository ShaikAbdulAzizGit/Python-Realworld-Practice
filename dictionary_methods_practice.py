# Dictionary methods 

# Task 1

request_data = {
    "user_id": 101,
    "email": "ali@gmail.com"
}

user_id=request_data.get('user_id','guest')
role=request_data.get('role','guest')

print(user_id)
print(role)

# Task 2

users = [
    {"name": "Ali", "role": "admin"},
    {"name": "Sara", "role": "user"},
    {"name": "John", "role": "admin"}
]


res={}

for user in users:
    res.setdefault(user['role'],[]).append(user['name'])


print(res)



# Task 3

default_config = {
    "debug": False,
    "timeout": 30
}

env_config = {
    "debug": True
}

default_config.update(env_config)

print(default_config)


# Task 4

user_data = {
    "id": 1,
    "name": "Ali",
    "password": "secret123",
    "token": "abcxyz"
}

user_data.pop('password',None)
user_data.pop('token',None)
print(user_data)

# Task 5

headers = {
    "Host": "example.com",
    "Content-Type": "application/json"
}

res='Authorization' in headers

print(res)

# Task 6

events = [
    {"type": "INFO"},
    {"type": "ERROR"},
    {"type": "INFO"},
    {"type": "WARNING"}
]

counts={}

for event in events:
    event_type=event['type']
    counts[event_type]=counts.get(event_type,0)+1

print(counts)

# Task 7

payload = {
    "name": "Ali",
    "email": None,
    "age": 25,
    "phone": None
}


res={k:v for k,v in payload.items() if v is not None}

print(res)


# Task 8

data = {
    "name": "Ali",
    "age": 25,
    "active": True
}


for key,value in data.items():
    print(f'{key} -> {value}')



# Task 9

cache = {
    "session": "abc",
    "user": "Ali"
}

cache.clear()
print(cache)

# Task 10

cache = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(cache.popitem())
print(cache)

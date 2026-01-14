# Dictionary methods 

# Task 1

request_data = {
    "user_id": 101,
    "email": "ali@gmail.com"
}

res=request_data.get('user_id','guest')

print(res)

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

if 'password' or 'token' in user_data.keys():
    user_data.pop('password')
    user_data.pop('token')
print(user_data)

# Task 5

headers = {
    "Host": "example.com",
    "Content-Type": "application/json"
}

res='Authorization' in headers

print(res)



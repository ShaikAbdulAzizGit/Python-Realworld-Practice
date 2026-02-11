# Problem 1: User Registration System (CLASS vs INSTANCE)

class User:
    total_users=0

    def __init__(self,user_id,email):
        self.user_id=user_id
        self.email=email
        User.total_users+=1
    def get_info(self):
        info=f'''
'User id : {self.user_id}
User email : {self.email}
'''
        return info
    @classmethod
    def get_total_users(cls):
        return cls.total_users
    

# Problem 2: Employee Salary Management

class Employee:
    salary_cap=65000
    def __init__(self,name,salary):
        self.name=name
        if self.salary>Employee.salary_cap:
            raise ValueError('Salary exceeds cap')
        self.salary=salary
    def increase_salary(self,amount):
        if self.salary+amount>Employee.salary_cap:
            raise ValueError('Amount exceeded the maximum salary compensation')
        self.salary+=amount
    def get_salary(self):
        return self.salary
    @classmethod
    def update_salary_cap(cls,new_cap):
        cls.salary_cap=new_cap


# Problem 3: Product Inventory System

class Product:
    total_products=0
    def __init__(self,product_id,stock):
        self.product_id=product_id
        self.stock=stock
        Product.total_products+=1
    def add_stock(self,quantity):
        if quantity<=0:
            raise ValueError('Quantity must be positive')
        self.stock+=quantity
    def remove_stock(self,quantity):
        if quantity<=0:
            raise ValueError('Quantity must be positive')
        if quantity>self.stock:
            raise ValueError('Insufficient stock')
        else:
            self.stock-=quantity
    def get_stock(self):
        return self.stock
    

# Problem 4: API Rate Limiter (IMPORTANT REAL WORLD)

class RateLimitExceed(Exception):
    pass
class RateLimiter:
    MAX_REQUESTS=5
    def __init__(self,user_id,request_count):
        self.user_id=user_id
        self.request_count=request_count
    def allow_request(self):
        if self.request_count<=RateLimiter.MAX_REQUESTS:
            self.request_count+=1
            return True
        else:
            return False
    def reset_requests(self):
        self.request_count=0
    

# Problem 5: Student Grading System

class Student:
    passing_marks=75
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_pass(self):
        return self.marks>=Student.passing_marks
    @classmethod
    def update_pass_marks(cls,new_marks):
        cls.passing_marks=new_marks
    

# Problem 6: Configuration Loader (REAL PROJECT STYLE)

class Config:
    supported_env = ('PATH', 'HOME', 'USERPROFILE', 'USER', 'PWD', 'SHELL', 'LANG', 'TEMP', 'SystemRoot', 'API_KEY', 'DATABASE_URL', 'APP_ENV')

    def __init__(self,env,settings):
        self.env=env
        self.settings=settings
    
    def is_valid_env(self):
        if self.env in Config.supported_env:
            return True
        return False
    def get_setting(self,key,default=None):
        return self.settings.get(key,default)
    

# Problem 7: Shopping Cart System

class ShoppingCart:
    cart_count=0
    def __init__(self):
        self.items=[]
        ShoppingCart.cart_count+=1
    def add_item(self,item):
        self.items.append(item)
    def remove_item(self,item):
        if item not in self.items:
            raise ValueError('Item not present in Added Items')
        self.items.remove(item)
    def get_total_items(self):
        return len(self.items)


# Problem 8: Application Session Manager (ADVANCED REAL WORLD)

class Session:
    active_sessions_count=0
    def __init__(self,session_id):
        self.session_id=session_id
        self.active=False
    def start(self):
        if not self.active:
            self.active=True
            Session.active_sessions_count+=1
    def end(self):
        if self.active:
            self.active=False
            Session.active_sessions_count-=1
    def get_active_sessions(self):
        return Session.active_sessions_count
    




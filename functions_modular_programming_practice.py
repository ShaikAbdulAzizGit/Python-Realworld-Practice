# Task 1

def validate_username(username):
    if len(username)>=4 and " " not in username:
        return True,None
    elif len(username)<4:
        return False , 'Username length must be greater than or equal to 4'
    elif " " in username:
        return False , 'Username must not contain white spaces'


def validate_password(password):
    has_upper=False
    has_lower=False
    has_digit=False

    if len(password) >= 8:
        for ch in password:
            if 'A' <= ch <= 'Z':
                has_upper=True

        for ch in password:
            if 'a' <= ch <= 'z':
                has_lower=True

        for ch in password:
            if '0' <= ch <= '9':
                has_digit=True

        if has_upper and has_lower and has_digit:
            return True , None
        elif not has_upper:
            return False , 'Password does not contain Upper case letter'
        elif not has_lower:
            return False , 'Password does not contain Lower case letter'
        elif not has_digit:
            return False , 'Password does not contain a digit'
    else:
        return False , 'Password lenght must be equal to or greater than 4'


def validate_age(age):
    if age >=18:
        return True , None
    else:
        return False , 'Age must be greater that or equal to 18'


def validate_user(username,password,age):
    if username !="" and password !="" and age !="":
        is_username_valid , username_error_message = validate_username(username)
        is_password_valid , password_error_message = validate_password(password)
        is_age_valid , age_error_message = validate_age(age)

        if is_username_valid and is_password_valid and is_age_valid :
            return "Registration Successful "
        elif not is_username_valid:
            return username_error_message
        elif not is_password_valid:
            return username_error_message
        elif not is_age_valid:
            return username_error_message
    else:
        return "Input fields cannot be empty"


try :
    user_name=input("Enter Username: ")
    user_password=input("Enter password: ")
    user_age=int(input("Enter Age : "))

    result=validate_user(user_name,user_password,user_age)
    print(f"Registration status : {result}")

except ValueError:
    print("Unexpected Input please enter the valid input value ")


# Task 2

def calculate_bonus(salary,experience):
    if experience < 2:
        bonus_percentage=5
    elif experience <=5:
        bonus_percentage=10
    elif experience > 5:
        bonus_percentage=20

    bonus = (bonus_percentage/100) * salary
    return bonus


def calculate_tax(salary_with_bonus):
    if salary_with_bonus > 50000:
        tax_percentage=10
    else:
        tax_percentage=5

    tax=(tax_percentage/100)*salary_with_bonus
    return tax


def calculate_final_salary(base_salary,experience):
    bonus=calculate_bonus(base_salary,experience)
    salary_with_bonus=base_salary+bonus
    tax=calculate_tax(salary_with_bonus)
    final_salary=salary_with_bonus-tax

    return {
        'base_salary':f'{base_salary}',
        'bonus':f'{bonus}',
        'tax':f'{tax}',
        'final_salary':f'{final_salary}'
    }


try:
    base_salary=int(input("Enter the base salary : "))
    experience=int(input("Enter the experience : "))

    final_salary_details=calculate_final_salary(base_salary,experience)
    print(final_salary_details)

except ValueError:
    print("Unexpected input please try again !.")


# Task 3

def count_even_odd(numbers):
    even_count=0
    odd_count=0

    for num in numbers:
        if num%2==0:
            even_count+=1
        else:
            odd_count+=1

    return even_count,odd_count


def get_min_max(numbers):
    max=0

    for num in numbers:
        if num>max:
            max=num

    min=max

    for num in numbers:
        if num<min:
            min=num

    return min,max


def get_average(numbers):
    number_of_values=len(numbers)
    sum_of_values=0

    for num in numbers:
        sum_of_values+=num

    average=sum_of_values/number_of_values
    return average


def filter_above_threshold(numbers, threshold=25):
    filtered_values=[]

    for num in numbers:
        if num>threshold:
            filtered_values.append(num)

    return filtered_values


numbers = [10, 15, 20, 25, 30, 35, 40]

even_count,odd_count=count_even_odd(numbers)
minimum_value,maximum_value=get_min_max(numbers)
average=get_average(numbers)
filtered_values=filter_above_threshold(numbers)

print(f"Even : {even_count} , Odd : {odd_count}")
print(f"Minimum value : {minimum_value} , Maximum value : {maximum_value}")
print(f"Average : {average}")
print(f"filtered_values: {filtered_values}")


# Task 4

def count_vowels(text):
    vowels=['a','e','i','o','u']
    vowels_count=0

    for ch in text:
        if ch in vowels:
            vowels_count+=1

    return vowels_count


def count_consonants(text):
    vowels=['a','e','i','o','u']
    consonant_count=0

    for ch in text:
        if ch not in vowels:
            consonant_count+=1

    return consonant_count


def count_digits(text):
    digits_count=0

    for ch in text:
        if '0' <= ch <= '9':
            digits_count+=1

    return digits_count


def text_summary(text):
    vowels_count=count_vowels(text)
    consonant_count=count_consonants(text)
    digits_count=count_digits(text)

    return {
        'vowels':f'{vowels_count}',
        'consonants':f'{consonant_count}',
        'digits':f'{digits_count}'
    }


text="Hello I am a python developer I enjoy writing code in python I am 19 years old"
result=text_summary(text)
print(result)


# Task 5
# ScholorShip Application

def input_utils():
    while True:
        try:
            student_name=input("Enter Student Name :").strip()
            class_level=int(input("Enter the which class the student belongs to "))
            annual_fee=int(input("Enter the yearly fee of the student "))
            break
        except ValueError:
            print("Unexpected input please try again !.")

    return student_name,class_level,annual_fee


def validation_utils(class_level,annual_fee):
    if class_level > 5 and annual_fee <=200000:
        return True , "Scholorship is approved"
    elif class_level<=5:
        return False, "Scholorship is rejected due to class must be more than 5"
    elif annual_fee>200000:
        return False, "Scholorship is rejected due to annual fee must be less than or equal to 200k"


def calculation_utils(annual_fee):
    if annual_fee <= 50000:
        scholorship_fee_percentage=75
    elif annual_fee <=100000:
        scholorship_fee_percentage=50
    elif annual_fee <=200000:
        scholorship_fee_percentage=25

    scholorship_fee=(scholorship_fee_percentage/100)*annual_fee
    return scholorship_fee


def main():
    student_name,class_level,annual_fee=input_utils()
    is_scholorship_approved,status_message=validation_utils(class_level,annual_fee)

    if is_scholorship_approved:
        scholorship_provided=calculation_utils(annual_fee)
        print(f'Scholorship Status :{status_message}')
        print(f'Scholorship fee provided :{scholorship_provided}')
    else:
        print(f'Scholorship Status{status_message}')


if __name__=="__main__":
    main()

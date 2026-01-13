# Task 1

USERNAME='admin'
PASSWORD='1234'
count=0

while True:
    if count >=3:
        print("Account Locked !..")
        break

    user_name=input('Please Enter User Name : ').strip()
    password=input('please Enter passoword : ')

    if user_name == USERNAME and password == password:
        print("Login Successful")
        break
    else:
        print("Incorrect Credentials ")
        count+=1


# Task 2

positive_count=0
negative_count=0
even_count=0
odd_count=0
total_numbers=0

print("Please Enter Numbers : ")

while True:
    try:
        val=int(input("Number: "))
    except Exception as e :
        print("Invalid value please try again: ",e)
        continue

    if val!=0:
        total_numbers+=1

        if val > 0 :
            positive_count+=1
        else:
            negative_count+=1

        if val % 2 ==0 :
            even_count+=1
        else:
            odd_count+=1
    else :
        print(f" Total Numbers : {total_numbers}")
        print(f" postive numbers : {positive_count}")
        print(f" negative numbers : {negative_count}")
        print(f" Even numbers : {even_count}")
        print(f" odd numbers : {odd_count}")
        break


# Task 3

while True:
    tax = 0
    try:
        base_salary=int(input("Enter the base Salary : "))
        experience=int(input("Enter the experience : "))
    except Exception as e :
        print("Invalid input try again ! ",e)

    if experience < 2 :
        bonus= (5 / 100 ) * base_salary
    elif 2>=experience<5:
        bonus= (10 / 100) * base_salary
    elif experience > 5 :
        bonus= (20 / 100) * base_salary

    salary = base_salary + bonus

    if salary > 50000 :
        tax = (10/100) * salary

    salary = salary - tax

    print(f"Base salary : {base_salary}")
    print(f"Bonus Amount : {bonus}")
    print(f"Tax Amount : {tax}")
    print(f"Final Salary : {salary}")

# Task 4

has_upper=False
has_lower=False
has_digit=False

user_password=input("Enter password here : ")

if len(user_password) >=8 :
    for ch in user_password:
        if 'A' <= ch <='Z':
            has_upper=True
        elif 'a' <= ch <='z':
            has_lower=True
        elif '0' <= ch <='9':
            has_digit=True

    if has_upper and has_lower and has_digit:
        print("The password in strong")
    else:
        if has_upper!=True:
            print("Password does not have a upper case letter ")
        if has_lower!=True:
            print("Password does not have a lower case letter ")
        if has_digit!=True:
            print("Password does not have a digit")
else:
    print("Password lenght is less than 8")


# Task 5

print(
    "1. Check even/odd",
    "2. Check positive/negative",
    "3. Find largest of 3 numbers",
    "4. Exit",
    sep='\n'
)

while True:
    try :
        user_choice=int(input("Enter your choice"))

        match user_choice:
            case 1:
                val = int(input("Enter the number :"))
                if val % 2 ==0 :
                    print(f"{val} is Even number ")
                else:
                    print(f"{val} is an odd number")

            case 2:
                val = int(input("Enter the number :"))
                if val > 0 :
                    print(f"{val} is Positive number ")
                else:
                    print(f"{val} is Negative number")

            case 3:
                val_1=int(input("Enter value 1 : "))
                val_2=int(input("Enter value 2 : "))
                val_3=int(input("Enter value 3 : "))

                if val_1 > val_2:
                    if val_1 > val_3:
                        print(f"{val_1} is greatest number")
                    else:
                        print(f"{val_3} is greatest number")
                else:
                    print(f"{val_2} is greatest number")

            case 4:
                break

            case _:
                print("Unexpected input try again ")

    except Exception as e :
        print("Please try again ")

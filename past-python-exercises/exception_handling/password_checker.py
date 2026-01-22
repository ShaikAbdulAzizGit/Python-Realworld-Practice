import re
class PasswordTooWeakError(Exception):
    pass
def check_password_strength(password):
    if len(password) < 8:
        raise PasswordTooWeakError("Password must be at least 8 characters long.")
    if not re.search(r"\d", password):
        raise PasswordTooWeakError("Password must contain at least one number.")
    if not re.search(r"[A-Z]", password):
        raise PasswordTooWeakError("Password must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        raise PasswordTooWeakError("Password must contain at least one lowercase letter.")
    if not re.search(r"[@$!%*?&]", password):
        raise PasswordTooWeakError("Password must contain at least one special character (@$!%*?&).")
    return True

def save_password(username,password):
    with open('user_password.txt','a') as f:
        f.write(f"username :{username}\npassword :{password}\n")

if __name__=="__main__":
    while True:
        username=input("Enter the username :")
        password=input("Enter the password :")
        try:
            if check_password_strength(password):
                save_password(username,password)
        except PasswordTooWeakError as e:
            print(f"Unable to register : {e}")
        finally:
            print("Password strength checking process is completed  successfully")



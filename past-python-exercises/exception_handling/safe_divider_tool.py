# Task 1
# try:
#     num_1=int(input("Enter the number 1 :"))
#     num_2=int(input("Enter the number 2 :"))
#     print(num_1/num_2)
# except (ZeroDivisionError,ValueError) as e :
#     print(f"Unexpected error : {e}")


# Task 2
# file_name=input("Enter the file name :").strip().replace(" ","_")
# try:
#     with open(file_name,'r',encoding="utf-8") as f:
#         file_content=f.read()
# except FileNotFoundError as e:
#     print(f"Unable to find file please try again : {e}")
# finally:
#     print("Done checking")


# Task 3
# def withdraw(balance,amount):
#     if amount>balance:
#         raise Exception("Insufficent balance")
#     else:
#         return balance-amount


# balance=4000
# try:
#     amount=int(input("Enter the amount to withdraw"))
# print(f"The current balance is {withdraw(balance,amount)}")
    


# class my_exception(Exception):
#     def __init__(self):
#         super().__init__("Helllo this is custom exception")



# check=False
# try:
#     if check:
#         pass
#     else:
#         raise my_exception()
# except my_exception as e:
#     print(e)

# print("Program completed")




class my_exception(Exception):
    pass



age=14
try:
    if age<18:
        raise my_exception("The is not satisfied to vote ")
    else:
        print("You can vote ")
except Exception as e:
    print(e)
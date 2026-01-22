import re,os
def remove_duplicates(file):
    with open(file,'r') as f:
        data_list=f.readlines()
    cleaned_data=[]
    for message in data_list:
        if message not in cleaned_data:
            cleaned_data.append(message)
    try:
        with open('cleaned_log.txt','w') as f:
            f.writelines(msg+'\n' for msg in cleaned_data)
            print("--cleaned_log file created successfully")
    except Exception as e:
        print(f"Ther is some problem please try again : {e}")
def get_error_messages(file):
    with open(file,'r') as f:
        data_list=f.readlines()
        error_messages=[]
    for message in data_list:
        if message.split()[0].lower()=='[error]':
            error_messages.append(message)
    with open('error_log.txt','a') as f:
            f.writelines(message+"\n" for message in error_messages)
            print("error_log file created successfully")

def get_sort_messages(file,type_message):
    with open(file,'r') as f:
        data_list=f.readlines()
    print("--sorted messages")
    sorted_messages=[]
    for message in data_list:
        if message.split()[0].lower()==f'[{type_message}]':
            sorted_messages.append(message)
    with open(f'{type_message}.txt','a') as f:
            f.writelines(message+"\n" for message in sorted_messages)
            print(f"{type_message} file created successfully")
def main(file):
    print("------------------------------")
    print("1. Remove duplicates")
    print("2. get error messages")
    print("3. sort based on message type")
    print("Choose [1,2,3]")
    print("------------------------------")
    user_input=input("Choose the operation (exit to stop): ").strip()
    if 'exit' in user_input.lower().strip():
        print("Exiting the program !..")
        exit()
    match user_input:
        case "1":
            remove_duplicates(file)
        case "2":
            get_error_messages(file)
        case "3":
            user_selection=input("Select the message type : ").lower().strip()
            if user_selection in ['error','warning','info']:
                get_sort_messages(file,user_selection)
            else:
                print("--Message type did not found !..")
        case _:
            print("--Unexpected input please try again")


if __name__=="__main__":
    while True:
        main('system.log')




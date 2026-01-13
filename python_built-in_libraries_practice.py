# Task 1

from datetime import datetime

user_name=input("Enter your name : ").strip()

now=datetime.now()

if user_name!="":
    with open('user_data.txt','a') as f:
        f.write(f'{user_name} | {now.date()} | {now.strftime('%H:%M:%S')}')
else:
    print("Please Enter a valid name !..")

# Task 2

import os,sys

path=input("Enter directory name : ").strip()

if os.path.isdir(path):
    all_files=os.listdir(path)
    temp_files=0
    print("All files before removing .temp files")
    print(all_files)
    for file in all_files:
        if file.endswith('.temp'):
            os.remove(os.path.join(path,file))
            temp_files+=1
    print(f"Total files scanned: {len(all_files)}")
    print("All files after removing .temp files")
    print(os.listdir(path))
    
else:
    print("There is no such directory exists or it might be a file !..")


# Task 3

import sys
import os

def get_lines(file_name):
    with open(file_name,'r') as f:
        file_data=f.readlines()
    return len(file_data)

def get_words(filename):
    with open(filename,'r') as f:
        words=f.read().split() 
    return len(words)   

def get_characters(filename):
    with open(filename,'r') as f:
        words=f.read().split()
    character_count=0
    for word in words:
        for ch in word:
            character_count+=1
    return character_count

if len(sys.argv)<2:
    print("Please Enter the atleast one variable name")
    sys.exit(1)

file_name=sys.argv[1]

if os.path.isfile(file_name):
    lines_count=get_lines(file_name)
    words_count=get_words(file_name)
    characters_count=get_characters(file_name)
    print(f"{file_name} contains : {lines_count} lines , {words_count} words , {characters_count} characters")
else:
    print(f'{file_name} does not exists as a file or its a directory')
    

# Task 4

from pathlib import Path


directory_name=input("Enter directory name : ").strip()

path=Path(directory_name)


if path.is_dir():
    python_files_count=len(list(path.rglob('*.py')))
    text_files_count=len(list(path.rglob('*.txt')))
    total_files_count=len(list(path.iterdir()))
    print(f"Python files : {python_files_count}")
    print(f"Text files : {text_files_count}")
    print(f"Total files : {total_files_count}")
else:
    print(f"{directory_name} does not exits as a directory")


# Task 5

import random 
from datetime import datetime,timedelta

def get_otp():
    otp=random.randint(100000,999999)
    expiration_time=datetime.now()+timedelta(minutes=2)
    return otp,expiration_time.time()

def validate_otp(generated_otp,user_entered_otp,expiration_time):
    if datetime.now().time()>expiration_time:
        return False,"Time Expired"
    elif generated_otp==user_entered_otp:
        return True,"Otp valid"
    else:
        return False,"Invalid Otp"


user_input=input("Enter G to generate otp : ").lower().strip()

if user_input=='g':
    otp,expiration_time=get_otp()
    print(f"Your otp : {otp}")
    user_input=input("Enter V to validate otp").lower().strip()
    if user_input=='v':
        while True:
            user_input=input("Enter otp:")
            if user_input.isdigit():
                if len(user_input)==6:
                    status,status_message=validate_otp(otp,int(user_input),expiration_time)
                    print(f"Otp status : {status_message}")
                    break
            else:
                print("Please enter valid 6 numbers")
    
else:
    print("Thank you !. have a nice day ")


# Task 6

import subprocess

command=['python','--version']

result=subprocess.run(command,check=True,capture_output=True,text=True)

print(result.stdout)



# Task 7

from pathlib import Path
import sys
import random
import string
from datetime import datetime
import os
import shutil
import subprocess

def scan_folder():
    while True:
        folder_name=input("Enter folder name : ").strip()
        path=Path(folder_name)
        if path.is_dir():
            all_log_files=list(path.glob('*.log'))
            if len(all_log_files)<1:
                print("There is no log file exist")
                sys.exit(1)
            else:
                return folder_name,all_log_files
        else:
            print(f"{folder_name} does not exist as folder or it may be a file !.. , Try again")

def create_backup_folder(main_folder,log_files):
    random_string="".join(random.choices(string.ascii_lowercase,k=4))
    date_time=datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_folder=os.path.join(main_folder,f'backup_{date_time}_{random_string}')
    os.makedirs(backup_folder)
    for file in log_files:
        shutil.copy2(str(file),backup_folder)
    return backup_folder
def get_size(backup_folder):
    all_files=os.listdir(backup_folder)
    full_size=0
    for file in all_files:
        size=os.path.getsize(os.path.join(backup_folder,file))
        full_size+=size
    return full_size

def format_size(bytes_count):
    KB = 1024
    MB = 1024 * KB
    GB = 1024 * MB

    if bytes_count < KB:
        return f"{bytes_count} Bytes"
    elif bytes_count < MB:
        return f"{bytes_count / KB:.2f} KB"
    elif bytes_count < GB:
        return f"{bytes_count / MB:.2f} MB"
    else:
        return f"{bytes_count / GB:.2f} GB"
def main():
    main_folder,log_files=scan_folder()
    backup_folder=create_backup_folder(main_folder,log_files)
    script_name=os.path.basename(sys.argv[0])
    python_version=subprocess.run(['python','--version'],check=True,capture_output=True,text=True)
    backup_folder_size_in_bytes=get_size(backup_folder)
    backup_folder_size=format_size(backup_folder_size_in_bytes)

    print('Log Archival Tool Started')
    print('-------------------------')
    print(f'Script Name    : {script_name}',
    f'Python Version    : {python_version.stdout}',
    f'Total Log Files    : {len(log_files)}',sep='\n')
    print(f'Backup Folder Created:\n{backup_folder}')
    print(f'Copied Files:')
    for file in log_files:
        print(f'-{os.path.basename(str(file))}')
    print(f'Total Archive Size:\n{backup_folder_size}')

    print("Status: Archive completed successfully")



main()

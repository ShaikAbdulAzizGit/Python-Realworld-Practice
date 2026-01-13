# Task 1

from pathlib import Path
import os

def get_directory_path():
    while True:
        directory_name=input("Enter directory : ").strip()
        path=Path(directory_name)
        if path.is_dir():
            return path.resolve()
        else:
            print(f'{directory_name} does not exists as a directory or it may be a file , Please try again with valid directory ')

def scan_directory(path):
    all_items=[item for item in path.iterdir()]
    return all_items

def filter_files(all_items):
    actual_files=[item for item in all_items if item.is_file()]
    return actual_files

def generate_new_name(files,base_name):
    serial_numbers=1
    filename_mapping={}
    for file in files:
        old_name=file.name
        new_name=f'{base_name}_{serial_numbers}{file.suffix}'
        filename_mapping[old_name]=new_name
        serial_numbers+=1
    return filename_mapping

def rename_files(files,filename_map):
    renamed_files_count=0
    for file in files:
        # new_name=os.path.join(file.parent,filename_map[file.name])
        new_name=file.parent/filename_map[file.name]
        file.rename(new_name)
        renamed_files_count+=1
    return renamed_files_count

def generate_report(filename_map,files_renamed):
    for old_name,new_name in filename_map.items():
        with open('report.txt','a') as f:
            f.write(f'old_name:{old_name}->new_name:{new_name}','\n')
    with open('report.txt','a') as f:
        f.write(f'Total files renamed:{files_renamed}\n')
    return Path('report.txt').resolve()
    
def print_summary(files_renamed,report_file_path):
    print(f'Successfully completed renaming all the files')
    print(f'No of files renamed : {files_renamed}')
    print(f'Location of file : {report_file_path}')

def main():
    directory_path=get_directory_path()
    all_items=scan_directory(directory_path)
    actual_files=filter_files(all_items)
    filename_map=generate_new_name(actual_files,'invoice')
    renamed_files_count=rename_files(actual_files,filename_map)
    report_path=generate_report(filename_map,renamed_files_count)
    print_summary(renamed_files_count,report_path)

if __name__=='__main__':
    main()

    
# Task 2

from pathlib import Path

def read_file():
    while True:
        file_path=input("Enter file name : ").strip()
        path=Path(file_path)
        if path.is_file() and path.name.endswith('.txt'):
            with open(file_path,'r') as f:
                all_rows=f.readlines()
            return all_rows
        else:
            print(f'{file_path} does not exists as a text file please try again with valid text file !..')

def parse_rows(all_rows):
    parsed_rows=[]
    for row in all_rows:
        name,age=row.split(',')
        parsed_rows.append((name,age))
    return parsed_rows

def clean_rows(parsed_rows):
    cleaned_rows=[]
    for name,age in parsed_rows:
        cleaned_name=name.strip().lower()
        cleaned_age=age.strip()
        cleaned_rows.append((cleaned_name,cleaned_age))
    return cleaned_rows


def validate_rows(cleaned_rows):
    valid_rows=[]
    invalid_rows=[]
    for name,age in cleaned_rows:
        if name and age:
            if age.isdigit():
                valid_rows.append((name,age))
            else:
                invalid_rows.append((name,age))
        else:
            invalid_rows.append((name,age))
    return valid_rows,invalid_rows

def write_clean_data(valid_rows):
    cleaned_data=[]
    for name,age in valid_rows:
        item=f'{name},{age}'
        cleaned_data.append(item)
    with open('cleaned_data.txt','w') as f:
        f.writelines(line+'\n' for line in cleaned_data)
    return len(cleaned_data),'cleaned_data.txt'



def write_invalid_data(invalid_rows):
    rejected_data=[]
    for name,age in invalid_rows:
        item=f'{name},{age}'
        rejected_data.append(item)
    with open('rejected_data.txt','w') as f:
        f.writelines(line+'\n' for line in rejected_data)
    return len(rejected_data),'rejected_data.txt'
    

def get_summary(total_rows,no_of_valid_rows,no_of_invalid_rows,valid_file_path,invalid_file_path):
    print("Task Completed successfully")
    print(f"No of Total rows : {total_rows}")
    print(f"No of valid rows : {no_of_valid_rows}")
    print(f"No of Invalid rows : {no_of_invalid_rows}")
    print(f"Cleaned data file path : {valid_file_path}")
    print(f"Rejected data file path : {invalid_file_path}")

def main():
    all_rows=read_file()
    parsed_rows=parse_rows(all_rows)
    cleaned_rows=clean_rows(parsed_rows)
    valid_rows,invalid_rows=validate_rows(cleaned_rows)
    no_of_valid_rows,cleaned_data_file_path=write_clean_data(valid_rows)
    no_of_invalid_rows,rejected_data_file_path=write_invalid_data(invalid_rows)
    get_summary(len(all_rows),no_of_valid_rows,no_of_invalid_rows,cleaned_data_file_path,rejected_data_file_path)

if __name__=='__main__':
    main()


# Task 3


from pathlib import Path
from datetime import datetime

def get_directory_path():
    while True:
        directory_path=input("Enter directory : ").strip()
        path=Path(directory_path)

        if path.is_dir():
            return path
        else:
            print(f'{directory_path} does not exist as a directory or it may be a file !..')

def scan_directory(directory_path):
    all_items=[item for item in directory_path.iterdir()]
    if len(all_items)<1:
        print('This directory does not contains any files , Try again !.')
        get_directory_path()
    else:
        return

def filter_log_files(directory_path):
    log_files=list(directory_path.glob('*.log'))
    return len(log_files),log_files

def read_log_files(log_files):
    log_messages=[]
    for file in log_files:
        with file.open(mode='r') as f:
            log_messages.extend(f.readlines())
    return  len(log_messages),log_messages
    

def analyze_log_levels(log_messages):
    info_messages_count=0
    error_messages_count=0
    warning_messages_count=0
    debug_messages_count=0
    for message in log_messages:
        if "INFO" in message:
            info_messages_count+=1
        elif  "ERROR" in message:
            error_messages_count+=1
        elif "WARNING" in message:
            warning_messages_count+=1
        elif "DEBUG" in message:
            debug_messages_count+=1

    
    return info_messages_count,error_messages_count,warning_messages_count,debug_messages_count
            

def generate_report(total_files_scanned,info_messages_count,error_messages_count,warning_messages_count,debug_messages_count):

    return f'''Date: {datetime.now().strftime('%Y-%m-%d')}
    Files scanned: {total_files_scanned}
    INFO: {info_messages_count}
    ERROR: {error_messages_count}
    WARNING: {warning_messages_count}
    DEBUG: {debug_messages_count} '''

def write_report_to_file(report_content):
    with open('report.txt','w') as f:
        f.write(report_content)
    print("report.txt file successfully created")

def print_summary(report_content):
    print(report_content)

def main():
    directory_path=get_directory_path()
    scan_directory(directory_path)
    log_files_count,all_log_files=filter_log_files(directory_path)
    log_messages_count,all_log_messages=read_log_files(all_log_files)
    info_messages_count,error_messages_count,warning_messages_count,debug_message_count=analyze_log_levels(all_log_messages)
    report_content=generate_report(log_files_count,info_messages_count,error_messages_count,warning_messages_count,debug_message_count)
    write_report_to_file(report_content)
    print_summary(report_content)



if __name__=='__main__':
    main()



# Task 5 
from pathlib import Path
import sys
import shutil

def read_config(config_file):

    config={}
    path=Path(config_file)
    if path.is_file():
        with open(config_file,'r') as f:
            for line in f:
                key,value=line.strip().split('=')
                config[key]=value
        return config
    else:
        print(f'{config_file} does not exist as a file ')
    sys.exit(1)
def get_source_directory_path(config):
    source_directory_path=config['source_dir']
    path=Path(source_directory_path)
    if path.is_dir():
        return path
    else:
        print(f'{source_directory_path} does not exist as a folder , Try again with valid directory')
        sys.exit(1)

def get_destination_directory_path(config):
    destination_directory=config['destination_dir']
    destination_directory_path=Path(destination_directory)
    destination_directory_path.mkdir(exist_ok=True)
    path=Path(destination_directory)
    if path.is_dir():
        return path
def scan_source_directory(source_directory_path):
    all_files=[]
    for item in source_directory_path.iterdir():
        if item.is_file():
            all_files.append(item)
    if len(all_files)>=1:
        return all_files
    else:
        print(f'{source_directory_path.path} does not contain any file , Try again with valid directory !..')
        sys.exit(1)

def filter_files(all_files,config):
    file_extension=config['file_extension']
    filtered_files=[]
    for file in all_files:
        if file.name.endswith(file_extension):
            filtered_files.append(file)
    
    if len(filtered_files)>=1:
        return filtered_files
    else:
        print(f'There does not exist any file matching {file_extension} in {all_files[0].parent.name} folder')
        sys.exit(1)

def copy_files(files,destination_dir):
    files_copied=[]
    for file in files:
        destination_path=destination_dir/file.name
        try:
            shutil.copy2(file,destination_path)
            print(f'{file.name} copied to {destination_dir.name}')
            files_copied.append(file.name)
        except shutil.SameFileError:
            print('Source and Destination are same')
        except PermissionError:
            print(f'Permission denied for {file.name}')
        except Exception as e:
            print(f'Error copying {file.name}')
    return files_copied
def generate_report(files_copied,config):
    if files_copied:
        return f'''
Automation Task: Config-Based File Copy
Source Directory: {config['source_dir']}
Destination Directory: {config['destination_dir']}
File Extension: {config['file_extension']}

Files Copied:
{files_copied}

Total Files Copied: {len(files_copied)}
Status: SUCCESS
'''
def print_report(report_content):
    print(report_content)
def write_report(report_content,config):
    file_name=config['report_file']
    try:
        with open(file_name,'w') as f:
            f.write(report_content)
    except Exception as e:
        print("File creation failed ",e)
    return Path(file_name).resolve()


def main():
    config=read_config('config.txt')
    source_directory_path=get_source_directory_path(config)
    destination_directory_path=get_destination_directory_path(config)
    all_files=scan_source_directory(source_directory_path)
    filtered_files=filter_files(all_files,config)
    copied_files=copy_files(filtered_files,destination_directory_path)
    report_content=generate_report(copied_files,config)
    print_report(report_content)
    report_file_path=write_report(report_content,config)


if __name__=='__main__':
    main()

# Task 6

from datetime import datetime

def notify_admin(task_name,status,summary):
    timestamp=datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    content=f'''
task : {task_name}
status : {status}
time : {timestamp}

summary : 
{summary}

'''
    with open('notification.txt','w') as f:
        f.write(content)
    return content

if __name__=='__main__':
    notify_admin(
        task_name='File Renaming',
        status='success',
        summary='All log files renamed successfully'
    )



# Task 7


from pathlib import Path
from datetime import datetime

def get_directory_path():
    while True:
        directory_path=input("Enter directory : ").strip()
        path=Path(directory_path)

        if path.is_dir():
            return path
        else:
            print(f'{directory_path} does not exist as a directory or it may be a file !..')

def scan_directory(directory_path):
    all_items=[item for item in directory_path.iterdir()]
    if len(all_items)<1:
        print('This directory does not contains any files , Try again !.')
        get_directory_path()
    else:
        return

def filter_log_files(directory_path):
    log_files=list(directory_path.glob('*.log'))
    return len(log_files),log_files

def read_log_files(log_files):
    log_messages=[]
    for file in log_files:
        with file.open(mode='r') as f:
            log_messages.extend(f.readlines())
    return  len(log_messages),log_messages
    

def analyze_log_levels(log_messages):
    info_messages_count=0
    error_messages_count=0
    warning_messages_count=0
    debug_messages_count=0
    for message in log_messages:
        if "INFO" in message:
            info_messages_count+=1
        elif  "ERROR" in message:
            error_messages_count+=1
        elif "WARNING" in message:
            warning_messages_count+=1
        elif "DEBUG" in message:
            debug_messages_count+=1

    
    return info_messages_count,error_messages_count,warning_messages_count,debug_messages_count
            

def generate_report(total_files_scanned,info_messages_count,error_messages_count,warning_messages_count,debug_messages_count):

    return f'''Date: {datetime.now().strftime('%Y-%m-%d')}
    Files scanned: {total_files_scanned}
    INFO: {info_messages_count}
    ERROR: {error_messages_count}
    WARNING: {warning_messages_count}
    DEBUG: {debug_messages_count} '''

def write_report_to_file(report_content):
    with open('report.txt','w') as f:
        f.write(report_content)
    print("report.txt file successfully created")

def print_summary(report_content):
    print(report_content)

def notify_admin(task_name,status,summary):
    timestamp=datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    content=f'''
task : {task_name}
status : {status}
time : {timestamp}

summary : 
{summary}

'''
    with open('notification.txt','w') as f:
        f.write(content)
    return content

def main():
    try:
        directory_path=get_directory_path()
        scan_directory(directory_path)
        log_files_count,all_log_files=filter_log_files(directory_path)
        log_messages_count,all_log_messages=read_log_files(all_log_files)
        info_messages_count,error_messages_count,warning_messages_count,debug_message_count=analyze_log_levels(all_log_messages)
        report_content=generate_report(log_files_count,info_messages_count,error_messages_count,warning_messages_count,debug_message_count)
        write_report_to_file(report_content)
        print_summary(report_content)
        notify_admin(
            task_name='Log Report Generator',
            status='SUCCESS',
            summary=report_content,
        )
    except Exception as e:
        notify_admin(
            task_name='Log Report Generator',
            status='FAILED',
            summary=str(e),
        )


if __name__=='__main__':
    main()

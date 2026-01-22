def get_comments(python_file):
    with open(python_file,'r') as f:
        all_data=f.readlines()
    comments=[]
    for line in all_data:
        if line.startswith("#"):
            comments.append(line)
    if len(comments)!=0:
        with open('comments.txt','w') as f:
            f.writelines(comments)
        print("comments.txt is created successfully")
    else:
        with open('comments.txt','w') as f:
            pass # To clear the comments.txt file 
        print("No comments found") 


get_comments('sample_data.py')
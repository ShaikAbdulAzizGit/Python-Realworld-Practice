import os
def add_note(note):
    with open('notes.txt','a') as f:
        f.write(f"-{note}\n")
        print("Note saved.")
def show_note():
    with open('notes.txt','r') as f:
        note=f.read()
        if note=="":
            print("Note is empty")
        else:
            print(note)
def exit_program():
    print("Exiting program. Goodbye!")
    exit()
while True:
    user_input=input("What do you want to do? (Type a note / 'show' / 'exit'):").strip()
    match user_input:
        case 'show':
            show_note()
        case 'exit':
            exit_program()
        case _:
            add_note(user_input)
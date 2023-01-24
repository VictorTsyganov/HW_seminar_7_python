def main_menu():
    print('menu_list')
    menu_list = [
        'Show_all_contacts',
        'Open_file',
        'Save_file',
        'New_contact',
        'Change_contact',
        'Del_contact',
        'Find_contact',
        'Exit'
    ]

    for i in range(len(menu_list)):
        print(f'\t{i+1}. {menu_list[i]}')

    while True:
        try:
            user_input = int(input('Enter_command: '))
            if type(user_input) == int and user_input in range(1, 9):
                return user_input
            else:
                print('Wrong_input')
        except:
            print('Wrong_input')
    
def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end=' ')
            for value in db[i].values():
                print(value, end=' ')
            print()

def db_success(db):
    if db:
        print(f'\tPhone book successfully opened.')
        return True
    else:
        print(f"\tPhone book is empty or didn't opened.")
        return False

def exit_program():
    print('Mission completed!')
    exit()

def new_contact():
    print('Create new contact')
    dict_new_contact= dict()
    dict_new_contact['lastname'] = input(f'\tInput lastname: ')
    dict_new_contact['firstname'] = input(f'\tInput firstname: ')
    dict_new_contact['phone'] = input(f'\tInput phone: ')
    dict_new_contact['comment'] = input(f'\tInput comment: ')
    return dict_new_contact
    
def find_contact(db: list):
    if db_success(db):
        my_find = input('Enter what you are looking for: ')
        print()
        ind = 1
        for i in range(len(db)):
            temp = ';'.join(db[i].values())
            if my_find.lower() in temp.lower():
                print(f"\t{ind}. {temp.replace(';', ' ')}")
                ind += 1
        if ind == 1:
            print(f'\tContact not found')
        print()

def del_contact(db: list):
    if db_success(db):
        show_all(db)
        while True:
            try:
                contact_for_del = int(input('Select the contact number to delete '))
                if type(contact_for_del) == int and contact_for_del in range(1, len(db) + 1):
                    deleted_contact = ';'.join(db[contact_for_del - 1].values())
                    print(f'\tContact deleted!')
                    return deleted_contact
                else:
                    print('Wrong_input')
            except:
                print('Wrong_input')

def change_contact(db: list):
    if db_success(db):
        show_all(db)
        while True:
            try:
                contact_for_change = int(input('Select the contact number to change '))
                if type(contact_for_change) == int and contact_for_change in range(1, len(db) + 1):
                    db[contact_for_change - 1]['lastname'] = input('Input new lastname ')
                    db[contact_for_change - 1]['firstname'] = input('Input new firstname ')
                    db[contact_for_change - 1]['phone'] = input('Input new phone ')
                    db[contact_for_change - 1]['comment'] = input('Input new comment ')
                    print(f'\tContact changed!')
                    return db
                else:
                    print('Wrong_input')
            except:
                print('Wrong_input')

def success_save():
    print(f'\tContact saved!')
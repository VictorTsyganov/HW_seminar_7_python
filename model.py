db_list = []

contact_info = ''

def read_db(path: str) -> list:
    global db_list
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip().split(';')
            id_dict['lastname']=line[0]
            id_dict['firstname']=line[1]
            id_dict['phone']=line[2]
            id_dict['comment']=line[3]
            db_list.append(id_dict)
        return my_list

def write_db(path: str):
    global db_list
    with open(path, 'r', encoding='UTF-8') as file:
        phone_list = file.readlines()
    if db_list:
        for item in db_list:
            contact = []
            for value in item.values():
                contact.append(value)
            new_contact = ';'.join(contact) + '\n'
            if not new_contact in phone_list:
                with open(path, 'a', encoding='UTF-8') as file:
                    file.writelines(new_contact)
        db_list = []

def del_info(path: str):
    global contact_info
    global db_list
    if contact_info:
        with open(path, 'r', encoding='UTF-8') as file:
            phone_list = file.readlines()
            new_list = []
            for item in phone_list:
                if not contact_info in item:
                    new_list.append(item)
            with open(path, 'w', encoding='UTF-8') as file:
                for item in new_list:
                    file.write(item)
            db_list = []

def change_info(path: str):
    global db_list
    if db_list:
        new_db = []
        for item in db_list:
            contact = []
            for value in item.values():
                contact.append(value)
            new_contact = ';'.join(contact) + '\n'
            new_db.append(new_contact)
        with open(path, 'w', encoding='UTF-8') as file:
            for item in new_db:
                file.write(item)
        db_list = []

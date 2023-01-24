import model
import view

def input_handler(inp: int):
    if inp == 1:
        view.show_all(model.db_list)
    if inp == 2:
        model.read_db('database.txt')
        view.db_success(model.db_list)
    if inp == 3:
        view.db_success(model.db_list)
        model.write_db('database.txt')
        view.success_save()
    if inp == 4:
        model.db_list.append(view.new_contact())
    if inp == 5:
        model.change_contact_info = view.change_contact(model.db_list)
        model.change_info('database.txt')
    if inp == 6:
        view.db_success(model.db_list)
        model.contact_info = view.del_contact(model.db_list)
        model.del_info('database.txt')
    if inp == 7:
        view.find_contact(model.db_list)
    if inp == 8:
        view.exit_program()
    else:
        pass

def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)
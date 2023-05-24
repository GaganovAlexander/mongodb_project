import db


def execute(command_name: str, command_func, num_of_args: int, *args):
    if len(args) != num_of_args:
        print(f"Command {command_name} have {num_of_args} arguments")
        return
    command_func(*args)

while True:
    try:
        command = input().split()
    except KeyboardInterrupt:
        print('\nStop command received')
        break
    if not command:
        continue
    
    match command[0]:
        case 'insertFromFile':
            execute('insertFromFile', db.data_manipulation.insert_from_file, 2, command[1], command[2].replace("'", '').replace('"', ''), *command[3:])
        case 'initDB':
            execute('initDB', db.init_db.init_db, 0)
        case 'delete':
            execute('delete', db.data_manipulation.delete, 2, *command[1:])
        case 'change':
            execute('change', db.data_manipulation.change, 4, *command[1:])
        case 'supplie':
            execute('supplie', db.work_functions.supplie, 3, *command[1:])
        case 'suppliesAndPurchases':
            execute('suppliesAndPurchases', db.data_functions.supplies_and_purchases, 0, *command[1:])
        case _:
            print(f"Command {command[0]} does not exist")
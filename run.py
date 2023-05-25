import db
from common_data.data_fill import init_db, make_job


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
            execute('initDB', init_db, 0, *command[1:])
        case 'delete':
            execute('delete', db.data_manipulation.delete, 2, *command[1:])
        case 'change':
            execute('change', db.data_manipulation.change, 4, *command[1:])
        case 'supply':
            execute('supply', db.work_functions.supply, 3, *command[1:])
        case 'purchase':
            execute('purchase', db.work_functions.purchase, 3, *command[1:])
        case 'suppliesAndPurchases':
            execute('suppliesAndPurchases', db.data_functions.supplies_and_purchases, 0, *command[1:])
        case 'topUpBalance':
            execute('topUpBalance', db.work_functions.top_up_balance, 2, *command[1:])
        case 'makeJob':
            execute('makeJob', make_job, 0, *command[1:])
        case 'rating':
            execute('rating', db.data_functions.rating, 0, *command[1:])
        case 'turnover':
            execute('turnover', db.data_functions.turnover, 0, *command[1:])
        case _:
            print(f"Command {command[0]} does not exist")
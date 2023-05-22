from db.init_db import init_db

while True:
    try:
        command = input().split()
    except KeyboardInterrupt:
        print('\nStop command received')
        break
    if not command:
        continue

    match command[0]:
        case 'init_db':
            init_db()
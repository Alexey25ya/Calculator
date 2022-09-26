from datetime import datetime as dt

def logger(data, result):
    time = dt.now().strftime('%m.%d.%Y - %H:%M')
    with open('log.csv', 'a') as file:
        file.write(f'{data}: {time} = {result}\n')
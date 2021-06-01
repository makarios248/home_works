# Создать эмуляцию системы входа и регистрации для пользователей.
# При запуске программы,
# пользователя должно спросить проходил ли он регистрацию
# на нашем ресурсе,
# если да,
# тогда предложить ему ввести логин и пароль от его учетной записи.
# Если данные верны вывести сообщение об успешном входе в систему,
# если нет тогда сообщить об это.
# Если пользователь не регистрировался на ресурсе,
# тогда спросить не желает ли он пройти регистрацию.
# Если желает,
# взять от него необходимые данные и вывести об успешной регистрации,
# если не желает регистрироватся - пожелать удачи.
# Данные о зарегестрированных пользователях хранить в файле 'users.txt',
# по желанию можете создать
# файл для логирования событий регистрации и входа.

import random
import datetime

with open('users.txt', 'r') as data:
    store = {}
    for i in data.readlines():
        key, val = i.strip().split(':')
        store[key] = val
# создаем словарь с логинами и паролями из файла 'users.txt'

user_account = input('Hello! Do you have an account?(yes/no) ')
# спрашиваем, есть ли у пользователя аккаунт на нашем ресурсе

if user_account == 'yes':
    while True:
        user = input('Your user name: ')
        password = input('Your password: ')
        key = False
        if not (user in store and store[user] == password):
            print('Your username or password didn\'t match. '
                  'Please try again.')
            continue
        if user in store and store[user] == password:
            print(f'Welcome, {user}!')
            with open('loggin.txt', 'a') as f_log:
                # добавить событие в логфайл
                f_log.write(f'User {user} was authenticated '
                            f'successfully at {datetime.datetime.now()}\n')

            break
else:
    invite_to_join = input('Do you want to create an account?(yes/no) ')
    # у пользоватлеля нет аккаунта, хочет ли он зарегистрироватся?

    if invite_to_join == 'yes':
        while True:
            new_user = input('Create Username: ')
            new_password = input('Create Password: ')
            key = False
            if new_user in store:
                print('That user has already exist. Try again')
                continue
            if new_user not in store:
                add_user = {new_user: new_password}
                store.update(add_user)
                with open('users.txt', 'a') as f_users:
                    f_users.writelines(
                        '{}:{}\n'.format(k, v) for k, v in add_user.items())
                print(f'Welcome, {new_user}!')
                with open('loggin.txt', 'a') as f_log:
                    # добавить событие в логфайл
                    f_log.write(f'User {new_user} created an account '
                                f'at {datetime.datetime.now()}\n')
                break
    else:
        print('See you around :)')
        # у пользователя нет аккаунта и не хочет регистрироваться

# LABS
# *************************ЗАДАЧА №6******************************
# Есть два файла whitelist.txt и blacklist.txt,
# наполните их именами и фамилиями пользователей.
# 1. Попросить пользователя ввести имя и фамилию;
# 2. Если имени нет в черном и белом списках,
# тогда добавить пользователя в whitelist.txt и вывести приветствие;
# 3. Если имя есть в белом списке, вывести приветствие;
# 4. Если имя в черном списке, тогда вывести сообщение, что имя в блоке.

name = input('Please, state your name: ').title()
surname = input('Please, state your surname: ').title()

with open('whitelist.txt', 'r+', encoding='utf-8') as f_white,\
     open('blacklist.txt', 'r+', encoding='utf-8') as f_black:
    whitelist = set(f_white.read().split('\n'))
    blacklist = set(f_black.read().split('\n'))
    name_check = f'{name} {surname}'
    if name_check in whitelist:
        print('Welcome!')
    elif name_check in blacklist:
        print('Your account is blocked')
    else:
        whitelist.add(name_check)
        f_white.seek(0)
        f_white.write('\n'.join(whitelist))
        print('Welcome!')


# *************************ЗАДАЧА №7******************************
# 1. Прочитать содержимое файлов whitelist.txt и blacklist.txt;
# 2. Сделать вывод не на экран, а в новый файл
# Вывод должен выглядеть так:
# 	Имя
# ХХХХХХХХХХХХХХХХХХХХ
# 	Имя
# ХХХХХХХХХХХХХХХХХХХХ
# 	...
#     Print Finished

with open('whitelist.txt', 'r', encoding='utf-8') as f_white,\
     open('blacklist.txt', 'r', encoding='utf-8') as f_black:
    whitelist = f_white.read().split('\n')
    blacklist = f_black.read().split('\n')
    with open('tessst.txt', 'w', encoding='utf-8') as file_list:
        print(*whitelist, *blacklist, sep='\nХХХХХХХХХХХХХХХХХХХХ\n',
              end='\n    Print Finished', file=file_list)


# *************************ЗАДАЧА №8******************************
# Климатическая лаборатория отслеживает высокую температуру в пяти
# разных городах в течение
# первой недели июля. Идеальной структурой данных для хранения этих
# данных может быть
# представление списка вложенное в представление словаря:
#
# {
#     'Kiev': [0, 0, 0, 0, 0, 0, 0],
#     'Odessa': [0, 0, 0, 0, 0, 0, 0],
#     'Lviv': [0, 0, 0, 0, 0, 0, 0],
#     'Chernihiv': [0, 0, 0, 0, 0, 0, 0],
#     'Kharkiv': [0, 0, 0, 0, 0, 0, 0]
# }
#
# 1. Создать такой словарь имея список городов
# cities = ['Kiev', 'Odessa', 'Lviv', 'Chernihiv', 'Kharkiv']
# 2. Температура во вложенных списках должна быть случайной.
# (Решить задачу двумя способами:
# 	цикл for,
# 	dict comprehension)

cities = ['Kiev', 'Odessa', 'Lviv', 'Chernihiv', 'Kharkiv']
city_temperature = {el: random.sample(range(20, 50), 7) for el in cities}
print(city_temperature)

cities2 = ['Kiev', 'Odessa', 'Lviv', 'Chernihiv', 'Kharkiv']
city_temp = {}
for i in cities2:
    city_temp.update({i: random.sample(range(20, 50), 7)})

print(city_temp)

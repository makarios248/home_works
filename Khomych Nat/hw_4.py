# *************************ЗАДАЧА №1******************************
# Реализовать алгоритм пузырьковой сортировки.
#
# *************************ЗАДАЧА №2******************************
# Написать программу которая просит у пользователя ввести его любимое число.
# Если ввод число, тогда поблагодорить пользователя за сотрудничество и
# завершить программу.
# Если ввод не число, тогда попросить его быть более внимательным и
# ввести именно число.
# Если неправильный ввод более 3 раз, перейти на более грубое предупреждение.
# Если неправильный ввод более 5 раз, дать пользователю последний шанс.
# Если ввод по прежнему не число, тогда обругать пользователя и
# завершить программу.


def bubble_sort(sort_list):
    """ сортировка списка методом пузырька  """
    if isinstance(sort_list, list):
        n = len(sort_list)
        count = 0
        for i in range(1, n):
            for j in range(0, n - i):
                if sort_list[j] > sort_list[j + 1]:
                    sort_list[j], sort_list[j + 1] = \
                        sort_list[j + 1], sort_list[j]
                    count += 1
        return sort_list


print(bubble_sort([1, 7, 9, 4, 2, 8, 3, 5, 0, 6]))


def favorite_number():
    """ Запрашиваем у пользователя его любимое число. Принимаются
     натуральные, вещественные и отрицательные числа """
    counter = 0  # считаем, сколько раз пользователь ввел число
    for i in range(6):
        user_number = input('Please, input your favorite number: ')
        counter += 1
        try:
            user_number.isdigit() or float(user_number)
            print('Thank you for the number!')
            return user_number
        except ValueError:
            # еще 5 попыток в случае некоректного ввода
            if counter < 3:
                print('Retry. Use only digits')
                continue
            elif counter < 5:
                # после 3-го ввода более грубое предупреждение
                print('Warning! Invalid input more then 3 times')
                continue
            elif counter == 5:
                # после 5-го ввода даем еще 1 попытку
                print('Okay, last chance')
                continue

        # после 6й попытки программа завершается
        print('It\'s not your day. Goodbye!')
        return None


number = favorite_number()

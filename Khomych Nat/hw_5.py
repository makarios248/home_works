# Реализуйте шифратор и дешифратор по шифру Цезаря.
# Спросить пользователя, что он хочет сделать -
# зашифровать или расшифровать файл.
# Если зашифровать, попросить у него ввести имя шифруемого файла,
# имя файла, который мы получим на выходе(зашифрованного)
# и ключ(ключем будет уроваень сдвига).
# Если расшифровать, попросить ввести имя зашифрованного файла,
# имя файла на выходе(расшифрованного) и ключ.


def program_mode_selection():
    """ Выбор пользователем режима программы - текст нужно
        зашифровать ("e") или расшифровать ("d") """
    program_mode = input('Do you want to encrypt (type "e") '
                         'or decrypt (type "d")? ').lower()
    while True:
        if program_mode not in ('e', 'd'):
            program_mode = input('Please, write "e" to encrypt '
                                 'and "d" to decrypt: ').lower()
        elif program_mode == 'e':
            return 'e'
        else:
            return 'd'


def choose_language():
    """ Выбор языка шифрования пользователем.
        Доступны английский ("en") и русский ("ru") """
    while True:
        language = input('What language is your text in (en or ru)? ').lower()
        if language not in ('ru', 'en'):
            print('Please, write "en" for English and "ru" for Russian')
        elif language == 'ru':
            ru_alphabet = [chr(i) for i in range(1072, 1104)]
            return ru_alphabet
        else:
            en_alphabet = [chr(i) for i in range(97, 123)]
            return en_alphabet


def is_valid_key(alphabet):
    """ Пользователь задает шаг сдвига.
        key - целое число от 0 до количества букв в афавите - 1 """
    while True:
        key = input('Enter an integer that will be the key when encrypting '
                    'text: ')
        try:
            key.isdigit() and 0 < int(key) < len(alphabet)
            return int(key)
        except ValueError:
            print('Retry. Use only digits')


def is_valid_file_name():
    """ Пользователь указывает имя шифруемого файла и файла,
        где сохранить итоговый текст """
    while True:
        source_file = input('Please, name the source file: ')
        if isinstance(source_file, str) is True:
            result_file = input('How to name a new file: ')
            if isinstance(result_file, str) is True:
                return source_file, result_file
            else:
                print('Not valid name')
        else:
            print('Not valid name')


def caesar_cipher(file_in, file_out, key, alphabet):
    """ Шифруем или расшифровуем текст из файла, который указал
        пользователь. Если файл пустой или отсутствует, то будет
        выведено сообщение об ошибке.
        Результат сохраняем в новый файл с именем,
        которое также задал пользователь """
    try:
        start = open(file_in, 'r', encoding='utf-8')
        text = start.read()
        start.close()
        if not text:
            print(f'File {file_in} is empty')
    except FileNotFoundError:
        print(f'File {file_in} was not found')
    else:
        result = []
        for i in text:
            if i in alphabet:
                result += alphabet[(alphabet.index(i) + key) % len(alphabet)]
            elif i.lower() in alphabet:
                result += alphabet[(alphabet.index(i.lower()) + key) %
                                   len(alphabet)].upper()
            else:
                result += i
        with open(file_out, 'a+', encoding='utf-8') as to_save:
            print(f'Text successfully encoded and saved to {file_out}')
            return to_save.write(''.join(result))


def main_menu():  # запуск программы
    print('Welcome to The Caesar Cipher.\nThis program encrypts and decrypts '
          'the text using the Caesar algorithm.')
    alphabet = choose_language()
    source_file, result_file = is_valid_file_name()
    key = is_valid_key(alphabet)
    if program_mode_selection() == 'e':
        caesar_cipher(source_file, result_file, key, alphabet)
    else:
        caesar_cipher(source_file, result_file, key * -1, alphabet)


main_menu()  # вызов программы

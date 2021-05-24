# Дан словарь такого типа:

sample_dict = {
   'class_a': {
      'student1': {
         'name': 'Misha',
         'marks': {
            'math': 90,
            'history': 85
         }
      }
   }
}

# 1. Вывести значение ключа "name";
print(sample_dict.get('class_a').get('student1').get('name'))


# 2. Вывести значение ключа "history";
print(sample_dict['class_a']['student1']['marks']['history'])


# 3. Добавить нового студента в "class_a",
# соответственно его "name" и "marks";
dict_student2 = {'student2': dict(name='Andrey',
                                  marks=dict(math=87, history=84)
                                  )
                 }

sample_dict['class_a'].update(dict_student2)
print(sample_dict)


# 4. Добавить новый класс со студентами
# (в sample_dict нужно добавить class_b, в котором будет 2 студента);
dict_class_b = {'class_b': dict(
    student1={'name': 'Viktor'},
    student2={'name': 'Alisa'},
)
}

sample_dict.update(dict_class_b)
print(sample_dict)


# 5. Добавить каждому студенту в "marks" предмет "physics" с оценкой;
sample_dict['class_a']['student1']['marks']['physics'] = 75
sample_dict['class_a']['student2']['marks']['physics'] = 96
sample_dict['class_b']['student1']['marks'] = {'physics': 81}
sample_dict['class_b']['student2']['marks'] = {'physics': 90}
print(sample_dict)


# 6. Подсчитать средний бал по каждому студенту

class_a_student1_avg_mark = round(
    sum(sample_dict['class_a']['student1']['marks'].values())
    / len(sample_dict['class_a']['student1']['marks'].values()), 2)

class_a_student2_avg_mark = round(
    sum(sample_dict['class_a']['student2']['marks'].values())
    / len(sample_dict['class_a']['student2']['marks'].values()), 2)

class_b_student1_avg_mark = round(
    sum(sample_dict['class_b']['student1']['marks'].values())
    / len(sample_dict['class_b']['student1']['marks'].values()), 2)

class_b_student2_avg_mark = round(
    sum(sample_dict['class_b']['student2']['marks'].values())
    / len(sample_dict['class_b']['student2']['marks'].values()), 2)


# 7. Создать словарь со средним баллом за каждого студента;

students_avg_marks = {
    'class_a_student1': class_a_student1_avg_mark,
    'class_a_student2': class_a_student2_avg_mark,
    'class_b_student1': class_b_student1_avg_mark,
    'class_b_student2': class_b_student2_avg_mark,
}

print(students_avg_marks)


# 8. Определить лучшего студента по успеваемости;

the_best_student = max(students_avg_marks.keys(),
                       key=students_avg_marks.get)
print(the_best_student)


# 9. Подсчитать средний бал по каждому классу
# (результат округлить до 2 знаков после запятой);

class_a_avg_mark = round(
    (class_a_student1_avg_mark + class_a_student2_avg_mark) / 2, 2)

class_b_avg_mark = round(
    (class_b_student1_avg_mark + class_b_student2_avg_mark) / 2, 2)

print(class_a_avg_mark)
print(class_b_avg_mark)


# 10. Создать словарь со средним баллом за классы;

class_avg_marks = {
    'class_a': class_a_avg_mark,
    'class_b': class_b_avg_mark,
}
print(class_avg_marks)

# 11. Определить лучший класс по успеваемости.

the_best_class = max(class_avg_marks.keys(), key=class_avg_marks.get)
print(the_best_class)


# *************************ЗАДАЧА №3******************************
# 1. Открыть тот же файл и перезаписать его содержимое
# на эту же строку в обратном порядке (задом на перед).

with open('new_file.txt', 'r+') as file:
    text = file.read()
    file.seek(0)
    file.write(text[::-1])

# *************************ЗАДАЧА №4******************************
# Содержимое файл:
#
# Рудковский К.
# Иванов О.
# Петров И.
# Дмитриев Н.
# Смирнова О.
# Керченских В.
# Котов Д.
# Иванов О.
# Бирюкова Н.
# Данилов П.
# Аранских В.
# Лемонов Ю.
# Олегова К.
# Данилов П.
# Смирнова О.
# Керченских В.
# Петров И.
# Стадкевич О.
# Васюченко А.
# Рудковский К.
# Пацук И.
#
# 1. Считать данные с файла и сохранить только уникальные значения;
# 2. Записать их в новый файл в алфавитном порядке
# (каждый элемент в новой строке).


with open('names.txt', 'r+', encoding='utf-8') as file1, \
        open('unique_names.txt', 'w+', encoding='utf-8') as file2:
    all_names = file1.read()
    unique_names_list = list(set(all_names.split('\n')))
    unique_names_list.sort()
    unique_names = '\n'.join(unique_names_list)
    file2.write(unique_names)

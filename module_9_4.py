from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

""" lambda-функцию для следующего выражения - list(map(?, first, second)).
    Результатом должен быть список совпадения букв в той же позиции:
    [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
    Где True - совпало, False - не совпало."""
print(list(map(lambda ft, sd: ft == sd, first, second)))

""" Замыкание: напишите функцию get_advanced_writer(file_name, принимающую название файла для записи"""


def get_advanced_writer(file_name):
    # Функция write_everything(*data_set), принимающая неограниченное количество данных любого типа
    def write_everything(*data_set):
        # обращение оператором with к file_name для записи всех данных data_set
        # !!! для добавления к существующей записи новых строк вместо 'w+' указать 'a+'
        with open(file_name, 'w+', encoding='utf-8') as file:
            for i in data_set:  # цикл перебора данных data_set
                # запись в file переведенных в строку данных i из data_set каждого с новой строки
                file.write(str(i) + '\n')

    # Функция get_advanced_writer возвращает функцию write_everything.
    return write_everything


# Исходные данные, результат в файле example.txt (Изначально файл - пустой).
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

"""Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк."""


class MysticBall:
    def __init__(self, *words):
        self.words = words

    """ метод __call__, который случайным образом выбирать слово из words и 
        возвращает его используя импортированную функцию choice"""
    def __call__(self):
        return choice(self.words)


# исходные данные для Метод __call__
first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Возможно', 'Определенно')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())

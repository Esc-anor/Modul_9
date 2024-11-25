class StepValueError(ValueError):  # Класc StepValueError, который наследуется от ValueError.
    def __init__(self, message):
        self.message = message
    #  pass


""" Создайте класс Iterator, который обладает следующими свойствами:
    Атрибуты объекта:
    start - целое число, с которого начинается итерация.
    stop - целое число, на котором заканчивается итерация.
    step - шаг, с которым совершается итерация.
    pointer - указывает на текущее число в итерации (изначально start)"""


class Iterator:
    def __init__(self, start, stop, step=1):  # метод инициализации атрибутов класса
        if self._step(step):  # присвоение self.step значения step при условии не равенства 0
            self.step = step
        # присвоение остальных значений атрибутам класса
        self.start = start
        self.stop = stop

    def _step(self, stp):  # метод проверки значения step на равенство 0 и формирование исключения
        if stp == 0:
            raise StepValueError('шаг не может быть равен 0')
        return True  # возврат при валидности значения

    # __iter__ - метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора.
    def __iter__(self):
        self.pointer = self.start  # присвоение значения start атрибуту self.pointer
        return self  # возврат метода атрибут pointer

    # метод __next__, увеличивающий атрибут pointer на step
    def __next__(self):
        res = self.pointer  # присвоение res значения pointer
        # условие проверки знака step и достижения pointer атрибута stop
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration()  # выход из итерации при выполнении условия
        self.pointer += self.step  # увеличение pointer на step
        return res  # возврат работы метода


# исходные данные и вывод на консоль при помощи цикла for
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as exc:
    print('Шаг указан неверно')
    print(exc.message)

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()

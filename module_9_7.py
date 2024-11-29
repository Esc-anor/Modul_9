""" Функция декоратор (is_prime), которая распечатывает "Простое",
    если результат 1ой функции будет простым числом и "Составное" в противном случае."""


def is_prime(func):
    def wrapper(*args):
        x = func(*args)
        # условие проверки числа на простое / составное и вывод на консоль
        if all((x % i) != 0 for i in range(2, int(x ** 0.5) + 1)):
            print('Простое')
        else:
            print('Составное')
        return x  # возврат результата func(*args)

    return wrapper  # возврат функции wrapper


@is_prime  # обращение к функции декоратору
def sum_three(*args):  # Функция, sum_three суммирующая любое количество числовых аргументов
    res = 0
    for i in args:
        res += i
    return res


result = sum_three(2, 3, 6)
print(result)

result2 = sum_three(10, 6, 15, 4)
print(result2)

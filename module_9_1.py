# объявление функции apply_all_func, которая вызывает функцию functions к списку int_list
def apply_all_func(int_list, *functions):
    results = {}  # объявление словаря result
    for f in functions:  # цикл перебора функций из *functions
        # формирование словаря result {функция: результат работы функции со списком}
        results[f.__name__] = f(int_list)
    return results  # возврат работы функции apply_all_func - словарь result


def min_arg(int_list):  # min - принимает список, возвращает минимальное значение из него.
    return min(int_list)


def max_arg(arg):  # max - принимает список, возвращает максимальное значение из него.
    return max(arg)


def len_arg(arg):  # len - принимает список, возвращает кол-во элементов в нём.
    return len(arg)


def sum_arg(arg):  # sum - принимает список, возвращает сумму его элементов.
    return sum(arg)


def sorted_arg(arg):  # sorted - принимает список, возвращает новый отсортированный список на основе переданного.
    return sorted(arg)


# исходные данные и вывод на консоль
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

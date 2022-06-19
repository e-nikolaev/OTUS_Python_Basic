"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number**2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    """
    Проверка, простое ли число
    Args:
        number (int): натуральное число для проверки
    Return:
        True / False
    """
    if number < 2:
        return False
    else:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
    return True


def filter_numbers(number_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(lambda x: x % 2, number_list))
    if filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, number_list))
    if filter_type == PRIME:
        return list(filter(is_prime, number_list))

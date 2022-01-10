import numpy

"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):

    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

    return(list(numpy.array(args) ** 2))


power_numbers([1, 2, 5, 7])

filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers():


# функция, которая фильтрует нечетные числа
def filter_even_num(in_num):
    if (in_num % 2) == 0:
        return True
    else:
        return False

# функция, которая фильтрует четные числа
def filter_odd_num(args):
    if (args % 2) == 0:
        return False
    else:
        return True

# функция, которая фильтрует натуральные числа
def is_prime(in_num):
    k = 0
    if in_num >= 2:
        for i in range(2, in_num // 2 + 1):
            if (in_num % i == 0):
                k = k + 1
        if (k <= 0):
            return True
        else:
            return False
    else:
        return False

    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

def filter_numbers(*args, t):
      if t is ODD:
        out_filter = filter(filter_odd_num, args)
        print("Отфильтрованный список: ", list(out_filter))
      elif t is EVEN:
          out_filter = filter(filter_even_num, args)
          print("Отфильтрованный список: ", list(out_filter))
      elif t is PRIME:
          out_filter = filter(is_prime, args)
          print("Отфильтрованный список: ", list(out_filter))


filter_numbers(2, 3, 4, 5, t=EVEN)


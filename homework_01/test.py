import numpy

def power_numbers(*args):
    print(list(numpy.array(args)**2))


power_numbers(1, 2, 5, 7)


# #filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

numbers = [1, 2, 4, 5, 7, 8, 10, 11, 3]


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


# не берем пример (не понятно)
# def is_prime(number):
#     if number&1 and number >= 3:
#         top = int(number**.5) + 1
#         for divisor in range(3, top, 2):
#             if not number%divisor: return False
#         return True
#     elif number == 2: return True
#     return False


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


#     """
#     функция, которая на вход принимает список из целых чисел,
#     и возвращает только чётные/нечётные/простые числа
#     (выбор производится передачей дополнительного аргумента)
#
#     >>> filter_numbers([1, 2, 3], ODD)
#     <<< [1, 3]
#     >>> filter_numbers([2, 3, 4, 5], EVEN)
#     <<< [2, 4]
#     """

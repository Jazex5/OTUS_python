import numpy


def power_numbers(*args):
    spisok = list(numpy.array(args)**2)
    return(spisok)

power_numbers(5,6,10)

# def square_nums(nums):
#     for i in nums:
#         print(i ** 2)
#
#
# square_nums([1, 2, 3, 4])


# """
#     функция, которая принимает N целых чисел,
#     и возвращает список квадратов этих чисел
#     >>> power_numbers(1, 2, 5, 7)
#     <<< [1, 4, 25, 49]
#    """

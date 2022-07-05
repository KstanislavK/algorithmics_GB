"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).
И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import randint
from timeit import timeit


def gnome_sort(lst_obj):
    i = 1
    while i < len(lst_obj):
        if not i or lst_obj[i - 1] <= lst_obj[i]:
            i += 1
        else:
            lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
            i -= 1
    return lst_obj[m]


m = 10
orig_list_10 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Длина {m}: '
      f'{timeit("gnome_sort(orig_list_10[:])", globals=globals(), number=100)}')

m = 100
orig_list_100 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Длина {m}: '
      f'{timeit("gnome_sort(orig_list_100[:])", globals=globals(), number=100)}')

m = 1000
orig_list_1000 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Длина {m}: '
      f'{timeit("gnome_sort(orig_list_1000[:])", globals=globals(), number=100)}')


# Длина 10: 0.0031868
# Длина 100: 0.3797821
# Длина 1000: 54.7335455

def without_sort(lst_obj):
    copy_lst = lst_obj[:]
    for i in range(len(lst_obj) // 2):
        copy_lst.remove(min(copy_lst))
    return min(copy_lst)


m = 10
org_list_10 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Длина = {m}: '
      f'{timeit("without_sort(orig_list_10)", globals=globals(), number=1000)}')

m = 100
org_list_100 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Длина = {m}: '
      f'{timeit("without_sort(orig_list_100)", globals=globals(), number=1000)}')

m = 1000
org_list_1000 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Длина = {m}: '
      f'{timeit("without_sort(orig_list_1000)", globals=globals(), number=1000)}')


# Длина = 10: 0.0050373999999999974
# Длина = 100: 0.28997779999999995
# Длина = 1000: 31.521301100000002
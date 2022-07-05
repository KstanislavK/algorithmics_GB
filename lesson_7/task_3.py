from numpy import median
from random import randint
from timeit import timeit


def numpy_median(lst_obj):
    return median(lst_obj[:])


m = 10
orig_list_10 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Длина = {m}: '
      f'{timeit("numpy_median(orig_list_10[:])", globals=globals(), number=1000)}')

m = 100
orig_list_100 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Длина = {m}: '
      f'{timeit("numpy_median(orig_list_100[:])", globals=globals(), number=1000)}')

m = 1000
orig_list_1000 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Длина = {m}: '
      f'{timeit("numpy_median(orig_list_1000[:])", globals=globals(), number=1000)}')


# Длина = 10: 0.0354651000816375
# Длина = 100: 0.05158049985766411
# Длина = 1000: 0.244003799976781
# Вывод:
# Встроенная функция самая эффективная
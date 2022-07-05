"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

from random import randint
from timeit import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_update(lst_obj):
    n = 1
    j = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                j += 1
        if j == 0:
            return lst_obj
        n += 1
    return lst_obj


# 10
orig_list_10 = [randint(-100, 100) for _ in range(10)]
print(timeit("bubble_sort(orig_list_10[:])", globals=globals(), number=1000))
print(timeit(
    "bubble_sort_update(orig_list_10[:])", globals=globals(), number=1000))

# 100
orig_list_100 = [randint(-100, 100) for _ in range(100)]
print(timeit("bubble_sort(orig_list_100[:])", globals=globals(), number=1000))
print(timeit(
    "bubble_sort_update(orig_list_100[:])", globals=globals(), number=1000))

# 1000
orig_list_1000 = [randint(-100, 100) for _ in range(1000)]
print(timeit("bubble_sort(orig_list_1000[:])", globals=globals(), number=1000))
print(timeit(
    "bubble_sort_update(orig_list_1000[:])", globals=globals(), number=1000))

print(orig_list_1000)
print(bubble_sort_update(orig_list_1000[:]))

"""
0.012653499999999998
0.0131446
0.6006225
0.7579523999999999
77.9412615
89.62397059999999
Вывод:
Не во всех случаях функция будет полезна. Все зависит от того, насколько
передаваемый массив уже упорядочен
"""
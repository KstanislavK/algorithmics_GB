"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""
import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

###############################


def func_lc(nums):
    lst = [n for n, el in enumerate(nums) if el % 2 == 0]
    return lst

##############################


NUMBERS = [num for num in range(1000)]

print(
    timeit.timeit(
        "func_1(NUMBERS)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_lc(NUMBERS)",
        globals=globals(),
        number=1000))


NUMBERS = [num for num in range(10000)]

print(
    timeit.timeit(
        "func_1(NUMBERS)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_lc(NUMBERS)",
        globals=globals(),
        number=1000))

NUMBERS = [num for num in range(100000)]

print(
    timeit.timeit(
        "func_1(NUMBERS)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_lc(NUMBERS)",
        globals=globals(),
        number=1000))

"""
Результаты замеров:
===1000===
0.19179639988578856
0.13056060019880533

===10000===
1.7342328000813723
1.656330999871716

===100000===
16.696819300064817
12.394151200074703

List compehensions отрабатывают заметно быстрее, чем обычные итераторы

"""
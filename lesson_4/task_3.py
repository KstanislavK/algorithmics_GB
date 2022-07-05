"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
Без аналитики задание считается не принятым
"""


import cProfile
from timeit import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(num):
    if num // 10 == 0:
        return str(num)
    else:
        return str(num - (num // 10) * 10) + str(revers_4(num // 10))


enter_num = 346346545745745742328078

revers_1(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)
revers_4(enter_num)


print(
    '=== Вариант 1 ===: ',
    timeit(
        f'revers_1({enter_num})',
        globals=globals(),
        number=10000))
print(
    '=== Вариант 2 ===: ',
    timeit(
        f'revers_2({enter_num})',
        globals=globals(),
        number=10000))
print(
    '=== Вариант 3 ===: ',
    timeit(
        f'revers_3({enter_num})',
        globals=globals(),
        number=10000))
print(
    '=== Вариант 4 ===: ',
    timeit(
        f'revers_4({enter_num})',
        globals=globals(),
        number=10000))

cProfile.run('revers_1(10000000000)')
cProfile.run('revers_2(10000000000)')
cProfile.run('revers_3(10000000000)')
cProfile.run('revers_4(10000000000)')


# === Вариант 1 ===:  0.06633719988167286
# === Вариант 2 ===:  0.04892119998112321
# === Вариант 3 ===:  0.0033672000281512737
# === Вариант 4 ===:  0.10910100000910461

"""
Третий вариант самый быстрый, т.к. в этом варианте не происходит вычислений, 
а преобразование проводится стандартной функцией
"""
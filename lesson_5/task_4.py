"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


common_dict = {}
od_dict = OrderedDict()
print('Добавление элементов')
print(timeit("""for i in range(10):
                    common_dict[i]=i""", globals=globals(), number=100000))
print(timeit("""for i in range(10):
                    od_dict[i]=i""", globals=globals(), number=100000))
print('Чтение')
print(timeit("""for i in range(10):
                    common_dict[i]""", globals=globals(), number=100000))
print(timeit("""for i in range(10):
                    od_dict[i]""", globals=globals(), number=100000))
print('Сравнение словарей')
print(timeit('common_dict == common_dict', globals=globals(), number=100000))
print(timeit('od_dict == od_dict', globals=globals(), number=100000))

# Добавление элементов
# 0.0715305998455733
# 0.08611579984426498
# Чтение
# 0.07674280018545687
# 0.07163719995878637
# Сравнение словарей
# 0.015653099864721298
# 0.019415000220760703
# Особой разницы между обычным и упорядоченным словарем не замечено.
# В версии 3.6 словари являются упорядоченными по-умолчанию.
# Стандартные словари в некотором роде удобнее, ведь не приходится думать о порядке.
# но в ситуациях, где порядок при сравнении критичен - необходим именно OrderedDict

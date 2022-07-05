"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача:
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.
В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""

from collections import deque
from timeit import timeit


def output(data):
    print(data[data.find(".")+1:data.find("(")], end=': ')
    print(f'{data[data.find("test"):data.find(".")]}',
          timeit(f'{data}', globals=globals(), number=1000))


if __name__ == '__main__':

    test_list = []
    test_deque = deque()

    n = [i for i in range(100)]

    # 1
    print('1')
    output("""for i in n:
                test_list.append(i)""")
    output("""for i in n:
                test_deque.append(i)""")
    output('test_list.pop()')
    output('test_deque.pop()')
    output('test_list.extend(n)')
    output('test_deque.extend(n)')

# append: test_list 0.0057252
# append: test_deque 0.005020000000000004
# pop: test_list 4.730000000000012e-05
# pop: test_deque 5.160000000000581e-05
# extend: test_list 0.0024857999999999963
# extend: test_deque 0.0011405999999999986
# Сильной разницы в скороси не обнаружено, т.к. обе структуры в операциях идентичны.
# Однако, операция extend работает немного быстрее.


    # 2
    print('2')
    output("""for i in n:
                    test_list.insert(0, i)""")
    output("""for i in n:
                    test_deque.appendleft(n)""")
    output('test_list.pop(0)')
    output('test_deque.popleft()')
    output("""for i in n:
                    test_list.insert(0, i)""")
    output('test_deque.extendleft(n)')

# insert: test_list
# 9.7186995
# appendleft: test_deque 0.005348599999999593
# pop: test_list 0.2719517000000007
# popleft: test_deque 0.00010650000000111959
# insert: test_list 13.824715499999998
# extendleft: test_deque 0.000974799999998055
# Видно, что операции "левого" добавления работают довольно медленно, т.к происходит постоянный пересчет индексов


    # 3
    print('3 часть')
    output("""for i in n: 
                test_list[i]""")
    output("""for i in n:      
                test_deque[i]""")


# 0.00389769999999956
# 0.004402999999999935
# Выборка работает немного быстрее, т.к список предназначен для произвольного доступа к данным.
# Дек же предназначен для выполнения операций с начала и конца массивов данных

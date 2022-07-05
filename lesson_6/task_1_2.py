from memory_profiler import memory_usage


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Время {mem_diff}")
        return res
    return wrapper


@memory
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@memory
def func_2(nums):
    return list(filter(lambda num: num % 2 == 0, nums))


num_list = list(range(100000))
func_1(num_list)
func_2(num_list)


# До оптимизации 2.57484375
# После оптимизации 0.45640625
# Заменил цикл на фильтр
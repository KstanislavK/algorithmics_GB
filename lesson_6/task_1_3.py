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
    for n in nums:
        if n % 2 == 0:
            yield n


array_nums = list(range(1000000))
func_1(array_nums)
func_2(array_nums)


# До оптимизации 18.0546875
# После оптимизации 0.0
# Использовал генератор yield
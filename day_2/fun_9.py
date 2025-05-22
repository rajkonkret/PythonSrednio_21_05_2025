import time
import tracemalloc
import numpy as np

from day_1.fun_5 import result

# pip install numpy
#  pip list

# tracemalloc.start()
array1 = np.arange(10_000_000, dtype=np.int8)
array2 = np.arange(10_000_000, dtype=np.int8)
current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()

# print(f"Current memory usage: {current / 1024 ** 2} MB;")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB;")
# print(array1.dtype)
# print(np.iinfo(array1.dtype))


# Current memory usage: 152.58807373046875 MB;
# Peak memory usage: 152.58807373046875 MB;
# int64
# Machine parameters for int64
# ---------------------------------------------------------------
# min = -9223372036854775808
# max = 9223372036854775807
# ---------------------------------------------------------------
# Current memory usage: 76.29412841796875 MB;
# Peak memory usage: 76.29412841796875 MB;
# int32
# Machine parameters for int32
# ---------------------------------------------------------------
# min = -2147483648
# max = 2147483647
# ---------------------------------------------------------------

# tracemalloc.start()
lista1 = list(range(10_000_000))
lista2 = list(range(10_000_000))


#
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
#
# print(f"Current memory usage: {current / 1024 ** 2} MB;")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB;")
# # Current memory usage: 762.9242553710938 MB;
# # Peak memory usage: 762.9243621826172 MB;
# Current memory usage: 19.07366943359375 MB;
# Peak memory usage: 19.07366943359375 MB;
# int8
# Machine parameters for int8
# ---------------------------------------------------------------
# min = -128
# max = 127
# ---------------------------------------------------------------
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure_time
def my_time():
    time.sleep(2)


@measure_time
def add_without_np():
    result = [lista1[i] + lista2[i] for i in range(len(lista1))]
    return "OK"


@measure_time
def add_zip():
    res = [a + b for a, b in zip(lista1, lista2)]
    return "OK ZIP"

@measure_time
def add_np():
    result = array1 + array2
    return "ok np"


my_time()  # Czas wykonania funkcji my_time: 2.0010130405426025
print(add_without_np())  # Czas wykonania funkcji add_without_np: 0.906005859375
print(add_zip())  # Czas wykonania funkcji add_zip: 0.8190057277679443
print(add_np())
# Sum is: 28
# Czas wykonania funkcji my_time: 2.0010156631469727
# Czas wykonania funkcji add_without_np: 0.924008846282959
# OK
# Czas wykonania funkcji add_zip: 0.7880074977874756
# OK ZIP
# Czas wykonania funkcji add_np: 0.009999275207519531
# ok np
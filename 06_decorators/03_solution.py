import time

def cache(func):
    cache_value = {}
    def wrapper(*args, **kwargs):
        print("cache value = ", cache_value)
        print("args = ",args)
        if args in cache_value:
            return cache_value[args]
        result = func(*args, **kwargs)
        print("result = ", result)
        cache_value[args] = result
        return result
    return wrapper


@cache
def long_running_funtion(a,b):
    time.sleep(4)
    return a+b


print(long_running_funtion(1,2))
print(long_running_funtion(1,2))
print(long_running_funtion(4,2))
print(long_running_funtion(6,2))
print(long_running_funtion(1,2))
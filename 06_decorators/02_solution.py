def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        print(args)
        print(kwargs)
        kwargs_value = ', '.join(f"{k}:{v}" for k, v in kwargs.items())
        print(f"calling {func.__name__} with arguments: {args_value} and kwargs: {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("Hello")

@debug
def greeting(name, greeting = "hello"):
    print(f"{greeting}, {name}")

# hello()
greeting("Umesh", greeting = "Hiiii")


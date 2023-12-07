import functools

def decorator_with_args_for_any_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Переданные арги и кварги в декоратор: {args} {kwargs}')
        return func
    return wrapper

@decorator_with_args_for_any_decorator
def decorated_decorator(func, *args, **kwargs):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)

decorated_function("Юзер", 101)
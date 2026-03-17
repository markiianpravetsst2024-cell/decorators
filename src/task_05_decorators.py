def double_result(func):
    """
    Decorator that multiplies the return value of `func` by 2.

    Example:
        >>> @double_result
        ... def add(a, b):
        ...     return a + b
        >>> add(2, 3)
        10
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result *= 2
        return result
    return wrapper



def repeat(times: int):
    """
    Decorator factory that calls the decorated function `times` times and
    returns a list of all results.

    The decorated function may accept any positional and keyword arguments.

    Args:
        times: How many times to call the function.

    Example:
        >>> @repeat(3)
        ... def say_hi():
        ...     return "hi"
        >>> say_hi()
        ['hi', 'hi', 'hi']

        >>> @repeat(2)
        ... def greet(name):
        ...     return f"Hello, {name}!"
        >>> greet("Ada")
        ['Hello, Ada!', 'Hello, Ada!']
    """


    def decorator(func):
        def wrapper(*args, **kwargs):

            return [func(*args, **kwargs) for i in range(times)]

        return wrapper

    return decorator
def sum_only_ints(*args) -> int:
    """
    Return the sum of all positional arguments that are exactly of type `int`.

    Rules:
        - Only count values whose type is exactly `int` (use `type()`, not `isinstance()`).
        - `bool` values must NOT be counted even though `bool` is a subclass of `int`.

    Example:
        >>> sum_only_ints(1, "a", 2, 3.5, True, 4)
        7
    """
    total = 0
    for arg in args:
        if type(arg) == int :
            total += arg
    return total


def build_user_profile(**kwargs) -> dict:
    """
    Return a new dictionary containing only the keys whose value is not None.

    Example:
        >>> build_user_profile(name="Anna", age=20, city=None)
        {'name': 'Anna', 'age': 20}
    """
    result = {}
    for key, value in kwargs.items():
        if value != None:
             result[key] = value
    return result

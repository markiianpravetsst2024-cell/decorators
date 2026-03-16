DEFAULT_PREFIX = "ID"


def make_counter(start: int = 0):
    """
    Return a closure `counter()` that generates sequential ID strings.

    Rules:
        - Each call to `counter()` increments the internal value by 1.
        - Use `nonlocal` to modify the counter state inside the closure.
        - Use the global `DEFAULT_PREFIX` to build the returned string.
        - The format is: "<PREFIX>-<value>"  e.g. "ID-1", "ID-2", ...
        - `start` shifts the sequence: make_counter(10) produces "ID-11", "ID-12", ...

    Example:
        >>> counter = make_counter()
        >>> counter()
        'ID-1'
        >>> counter()
        'ID-2'

        >>> counter2 = make_counter(10)
        >>> counter2()
        'ID-11'
    """
    raise NotImplementedError

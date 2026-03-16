def transform_and_filter(values: list[int], transform, predicate) -> list[int]:
    """
    Apply `transform` to every element in `values`, then keep only the elements
    for which `predicate` returns True.

    Args:
        values:     Input list of integers.
        transform:  A callable applied to each element  (e.g. lambda x: x * 2).
        predicate:  A callable used to filter results   (e.g. lambda x: x > 4).

    Returns:
        A list of transformed values that satisfy the predicate.

    Example:
        >>> transform_and_filter([1, 2, 3, 4], lambda x: x * 2, lambda x: x > 4)
        [6, 8]
    """
    raise NotImplementedError

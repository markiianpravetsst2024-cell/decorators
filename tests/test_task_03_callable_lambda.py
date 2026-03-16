from src.task_03_callable_lambda import transform_and_filter


def test_double_and_filter_greater_than_4():
    inp = [1, 2, 3, 4]
    result = transform_and_filter(inp, lambda x: x * 2, lambda x: x > 4)
    assert result == [6, 8], (
        f"Input   : {inp}\n"
        f"  transform : x * 2  →  [2, 4, 6, 8]\n"
        f"  predicate : x > 4  →  keeps 6 and 8\n"
        f"  Expected  : [6, 8]\n"
        f"  Got       : {result}"
    )


def test_all_filtered_out():
    inp = [1, 2, 3]
    result = transform_and_filter(inp, lambda x: x * 2, lambda x: x > 100)
    assert result == [], (
        f"Input   : {inp}\n"
        f"  transform : x * 2  →  [2, 4, 6]\n"
        f"  predicate : x > 100  →  nothing passes\n"
        f"  Expected  : []\n"
        f"  Got       : {result}"
    )


def test_none_filtered_out():
    inp = [1, 2, 3]
    result = transform_and_filter(inp, lambda x: x + 1, lambda x: x > 0)
    assert result == [2, 3, 4], (
        f"Input   : {inp}\n"
        f"  transform : x + 1  →  [2, 3, 4]\n"
        f"  predicate : x > 0  →  all pass\n"
        f"  Expected  : [2, 3, 4]\n"
        f"  Got       : {result}"
    )


def test_empty_input():
    result = transform_and_filter([], lambda x: x * 10, lambda x: True)
    assert result == [], (
        f"Input   : []\n"
        f"  Expected  : []  — empty input must return empty list\n"
        f"  Got       : {result}"
    )


def test_returns_list():
    result = transform_and_filter([1, 2], lambda x: x, lambda x: True)
    assert isinstance(result, list), (
        f"Input   : [1, 2]\n"
        f"  Expected return type : list\n"
        f"  Got                  : {type(result).__name__}  →  {result}"
    )


def test_named_functions_work():
    def square(x):
        return x * x

    def is_even(x):
        return x % 2 == 0

    inp = [1, 2, 3, 4]
    result = transform_and_filter(inp, square, is_even)
    assert result == [4, 16], (
        f"Input   : {inp}\n"
        f"  transform : square  →  [1, 4, 9, 16]\n"
        f"  predicate : is_even →  keeps 4 and 16\n"
        f"  Expected  : [4, 16]\n"
        f"  Got       : {result}"
    )


def test_identity_transform_with_filter():
    inp = [10, 20, 5, 15]
    result = transform_and_filter(inp, lambda x: x, lambda x: x >= 10)
    assert result == [10, 20, 15], (
        f"Input   : {inp}\n"
        f"  transform : identity (x)\n"
        f"  predicate : x >= 10  →  drops 5\n"
        f"  Expected  : [10, 20, 15]\n"
        f"  Got       : {result}"
    )

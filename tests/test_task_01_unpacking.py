from src.task_01_unpacking import split_first_last


def test_four_elements():
    inp = [10, 20, 30, 40]
    result = split_first_last(inp)
    assert result == (10, [20, 30], 40), (
        f"Input: {inp}\n"
        f"  Expected : (10, [20, 30], 40)\n"
        f"  Got      : {result}"
    )


def test_three_elements():
    inp = [1, 2, 3]
    result = split_first_last(inp)
    assert result == (1, [2], 3), (
        f"Input: {inp}\n"
        f"  Expected : (1, [2], 3)\n"
        f"  Got      : {result}"
    )


def test_two_elements_empty_middle():
    inp = [1, 2]
    result = split_first_last(inp)
    assert result == (1, [], 2), (
        f"Input: {inp}\n"
        f"  Expected : (1, [], 2)  — middle must be an empty list when there are only 2 elements\n"
        f"  Got      : {result}"
    )


def test_returns_tuple():
    inp = [1, 2, 3]
    result = split_first_last(inp)
    assert isinstance(result, tuple), (
        f"Input: {inp}\n"
        f"  Expected return type : tuple\n"
        f"  Got                  : {type(result).__name__}  →  {result}"
    )


def test_middle_is_list():
    inp = [1, 2, 3, 4]
    _, middle, _ = split_first_last(inp)
    assert isinstance(middle, list), (
        f"Input: {inp}\n"
        f"  Expected middle element type : list\n"
        f"  Got                          : {type(middle).__name__}  →  {middle}"
    )


def test_five_elements():
    inp = [5, 4, 3, 2, 1]
    result = split_first_last(inp)
    assert result == (5, [4, 3, 2], 1), (
        f"Input: {inp}\n"
        f"  Expected : (5, [4, 3, 2], 1)\n"
        f"  Got      : {result}"
    )


def test_negative_numbers():
    inp = [-3, -2, -1]
    result = split_first_last(inp)
    assert result == (-3, [-2], -1), (
        f"Input: {inp}\n"
        f"  Expected : (-3, [-2], -1)\n"
        f"  Got      : {result}"
    )


def test_identical_values():
    inp = [7, 7, 7, 7]
    result = split_first_last(inp)
    assert result == (7, [7, 7], 7), (
        f"Input: {inp}\n"
        f"  Expected : (7, [7, 7], 7)\n"
        f"  Got      : {result}"
    )

from src.task_02_args_kwargs import sum_only_ints, build_user_profile


# --- sum_only_ints ---

def test_sum_basic():
    args = (1, 2, 3)
    result = sum_only_ints(*args)
    assert result == 6, (
        f"Input: {args}\n"
        f"  Expected : 6\n"
        f"  Got      : {result}"
    )


def test_sum_skips_strings():
    args = (1, "a", 2)
    result = sum_only_ints(*args)
    assert result == 3, (
        f"Input: {args}\n"
        f"  Expected : 3  — strings must be ignored\n"
        f"  Got      : {result}"
    )


def test_sum_skips_floats():
    args = (1, 2, 3.5)
    result = sum_only_ints(*args)
    assert result == 3, (
        f"Input: {args}\n"
        f"  Expected : 3  — floats must be ignored\n"
        f"  Got      : {result}"
    )


def test_sum_skips_bools():
    args = (True, False, 1, 2)
    result = sum_only_ints(*args)
    assert result == 3, (
        f"Input: {args}\n"
        f"  Expected : 3  — bool values must NOT be counted (use type() not isinstance())\n"
        f"  Got      : {result}"
    )


def test_sum_mixed():
    args = (1, "a", 2, 3.5, True, 4)
    result = sum_only_ints(*args)
    assert result == 7, (
        f"Input: {args}\n"
        f"  Expected : 7  — only plain int values: 1 + 2 + 4\n"
        f"  Got      : {result}"
    )


def test_sum_no_ints():
    args = ("x", 1.5, True)
    result = sum_only_ints(*args)
    assert result == 0, (
        f"Input: {args}\n"
        f"  Expected : 0  — no plain int values present\n"
        f"  Got      : {result}"
    )


def test_sum_no_args():
    result = sum_only_ints()
    assert result == 0, (
        f"Input: (no arguments)\n"
        f"  Expected : 0\n"
        f"  Got      : {result}"
    )


def test_sum_returns_int():
    result = sum_only_ints(1, 2)
    assert type(result) is int, (
        f"Input: (1, 2)\n"
        f"  Expected return type : int\n"
        f"  Got                  : {type(result).__name__}  →  {result}"
    )


# --- build_user_profile ---

def test_profile_filters_none():
    kwargs = dict(name="Anna", age=20, city=None)
    result = build_user_profile(**kwargs)
    expected = {"name": "Anna", "age": 20}
    assert result == expected, (
        f"Input: {kwargs}\n"
        f"  Expected : {expected}  — keys with None must be dropped\n"
        f"  Got      : {result}"
    )


def test_profile_all_present():
    kwargs = dict(name="Bob", age=30)
    result = build_user_profile(**kwargs)
    expected = {"name": "Bob", "age": 30}
    assert result == expected, (
        f"Input: {kwargs}\n"
        f"  Expected : {expected}\n"
        f"  Got      : {result}"
    )


def test_profile_all_none():
    kwargs = dict(x=None, y=None)
    result = build_user_profile(**kwargs)
    assert result == {}, (
        f"Input: {kwargs}\n"
        f"  Expected : {{}}  — all values are None, result must be empty\n"
        f"  Got      : {result}"
    )


def test_profile_empty():
    result = build_user_profile()
    assert result == {}, (
        f"Input: (no arguments)\n"
        f"  Expected : {{}}\n"
        f"  Got      : {result}"
    )


def test_profile_zero_and_false_are_kept():
    kwargs = dict(score=0, active=False, label=None)
    result = build_user_profile(**kwargs)
    expected = {"score": 0, "active": False}
    assert result == expected, (
        f"Input: {kwargs}\n"
        f"  Expected : {expected}  — 0 and False are not None, they must be kept\n"
        f"  Got      : {result}"
    )


def test_profile_returns_dict():
    result = build_user_profile(a=1)
    assert isinstance(result, dict), (
        f"Input: (a=1)\n"
        f"  Expected return type : dict\n"
        f"  Got                  : {type(result).__name__}  →  {result}"
    )

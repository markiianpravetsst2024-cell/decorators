from src.task_04_scope import make_counter, DEFAULT_PREFIX


def test_default_prefix_value():
    assert DEFAULT_PREFIX == "ID", (
        f"  Expected DEFAULT_PREFIX : 'ID'\n"
        f"  Got                     : {DEFAULT_PREFIX!r}"
    )


def test_counter_starts_at_one():
    counter = make_counter()
    result = counter()
    assert result == "ID-1", (
        f"  make_counter() → first call\n"
        f"  Expected : 'ID-1'\n"
        f"  Got      : {result!r}"
    )


def test_counter_increments():
    counter = make_counter()
    counter()
    result = counter()
    assert result == "ID-2", (
        f"  make_counter() → second call\n"
        f"  Expected : 'ID-2'\n"
        f"  Got      : {result!r}"
    )


def test_counter_sequence():
    counter = make_counter()
    results = [counter() for _ in range(4)]
    expected = ["ID-1", "ID-2", "ID-3", "ID-4"]
    assert results == expected, (
        f"  make_counter() → 4 consecutive calls\n"
        f"  Expected : {expected}\n"
        f"  Got      : {results}"
    )


def test_counter_with_start():
    counter = make_counter(10)
    result = counter()
    assert result == "ID-11", (
        f"  make_counter(10) → first call\n"
        f"  Expected : 'ID-11'  — start shifts the sequence by 10\n"
        f"  Got      : {result!r}"
    )


def test_counter_with_start_increments():
    counter = make_counter(10)
    counter()
    result = counter()
    assert result == "ID-12", (
        f"  make_counter(10) → second call\n"
        f"  Expected : 'ID-12'\n"
        f"  Got      : {result!r}"
    )


def test_independent_counters():
    c1 = make_counter()
    c2 = make_counter()
    c1()
    c1()
    r1 = c1()
    r2 = c2()
    assert r1 == "ID-3", (
        f"  c1 called 3 times\n"
        f"  Expected : 'ID-3'\n"
        f"  Got      : {r1!r}"
    )
    assert r2 == "ID-1", (
        f"  c2 called 1 time (must be independent from c1)\n"
        f"  Expected : 'ID-1'\n"
        f"  Got      : {r2!r}"
    )


def test_counter_returns_string():
    counter = make_counter()
    result = counter()
    assert isinstance(result, str), (
        f"  make_counter() → first call\n"
        f"  Expected return type : str\n"
        f"  Got                  : {type(result).__name__}  →  {result!r}"
    )

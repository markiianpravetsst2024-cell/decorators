from src.task_05_decorators import double_result, repeat


# --- double_result ---

def test_double_result_basic():
    @double_result
    def add(a, b):
        return a + b

    result = add(2, 3)
    assert result == 10, (
        f"  @double_result on add(2, 3)\n"
        f"  add returns 5, decorator must multiply by 2\n"
        f"  Expected : 10\n"
        f"  Got      : {result}"
    )


def test_double_result_zero():
    @double_result
    def zero():
        return 0

    result = zero()
    assert result == 0, (
        f"  @double_result on zero()\n"
        f"  zero returns 0, 0 * 2 = 0\n"
        f"  Expected : 0\n"
        f"  Got      : {result}"
    )


def test_double_result_negative():
    @double_result
    def negate(x):
        return -x

    result = negate(3)
    assert result == -6, (
        f"  @double_result on negate(3)\n"
        f"  negate returns -3, -3 * 2 = -6\n"
        f"  Expected : -6\n"
        f"  Got      : {result}"
    )


def test_double_result_float():
    @double_result
    def half(x):
        return x / 2

    result = half(3)
    assert result == 3.0, (
        f"  @double_result on half(3)\n"
        f"  half returns 1.5, 1.5 * 2 = 3.0\n"
        f"  Expected : 3.0\n"
        f"  Got      : {result}"
    )


# --- repeat ---

def test_repeat_returns_list():
    @repeat(3)
    def say_hi():
        return "hi"

    result = say_hi()
    assert result == ["hi", "hi", "hi"], (
        f"  @repeat(3) on say_hi()\n"
        f"  Expected : ['hi', 'hi', 'hi']\n"
        f"  Got      : {result}"
    )


def test_repeat_once():
    @repeat(1)
    def value():
        return 42

    result = value()
    assert result == [42], (
        f"  @repeat(1) on value()\n"
        f"  Expected : [42]\n"
        f"  Got      : {result}"
    )


def test_repeat_zero_times():
    @repeat(0)
    def value():
        return 99

    result = value()
    assert result == [], (
        f"  @repeat(0) on value()\n"
        f"  Expected : []  — called 0 times, result must be empty list\n"
        f"  Got      : {result}"
    )


def test_repeat_with_args():
    @repeat(2)
    def greet(name):
        return f"Hello, {name}!"

    result = greet("Ada")
    assert result == ["Hello, Ada!", "Hello, Ada!"], (
        f"  @repeat(2) on greet('Ada')\n"
        f"  Expected : ['Hello, Ada!', 'Hello, Ada!']\n"
        f"  Got      : {result}"
    )


def test_repeat_with_kwargs():
    @repeat(2)
    def greet(name="World"):
        return f"Hi, {name}!"

    result = greet(name="Alice")
    assert result == ["Hi, Alice!", "Hi, Alice!"], (
        f"  @repeat(2) on greet(name='Alice')\n"
        f"  Expected : ['Hi, Alice!', 'Hi, Alice!']\n"
        f"  Got      : {result}"
    )


def test_repeat_with_args_and_kwargs():
    @repeat(3)
    def combine(a, b, sep="-"):
        return f"{a}{sep}{b}"

    result = combine(1, 2, sep=":")
    assert result == ["1:2", "1:2", "1:2"], (
        f"  @repeat(3) on combine(1, 2, sep=':')\n"
        f"  Expected : ['1:2', '1:2', '1:2']\n"
        f"  Got      : {result}"
    )

# Python Functions, Scope & Decorators — Homework

Practice packing/unpacking, `*args`/`**kwargs`, callables, scope, and decorators through five focused tasks.

---

## Setup

```bash
# 1. Clone the repository
git clone <repo-url>
cd python-functions-scope-decorators-homework

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the tests
pytest
```

All tests will fail at first — that is expected. Your job is to make them pass.

---

## Tasks

All tasks live in the `src/` folder. Each file contains function stubs with docstrings. Replace `raise NotImplementedError` with your implementation.

| File | Topic |
|------|-------|
| `src/task_01_unpacking.py` | Packing and unpacking |
| `src/task_02_args_kwargs.py` | `*args` and `**kwargs` |
| `src/task_03_callable_lambda.py` | Functions as arguments and lambdas |
| `src/task_04_scope.py` | Global, local, and nonlocal variables |
| `src/task_05_decorators.py` | Decorators and decorator factories |

Do **not** modify anything inside `tests/`.

---

## Running a single test file

```bash
pytest tests/test_task_01_unpacking.py
pytest tests/test_task_01_unpacking.py -v   # verbose output
```

---

## Submitting your work

1. **Fork** this repository on GitHub.
2. Create a new branch:
   ```bash
   git checkout -b solution/your-name
   ```
3. Commit your changes:
   ```bash
   git add src/
   git commit -m "Add solution"
   ```
4. Push the branch:
   ```bash
   git push origin solution/your-name
   ```
5. Open a **Pull Request** from your fork's branch to the original `main` branch.

Make sure all tests pass locally before opening the PR.

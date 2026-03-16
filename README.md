# Python Functions, Scope & Decorators — Homework

A beginner-to-intermediate Python homework assignment focusing on functions, scope, and decorators.

## Tasks

You will implement functions across five files:

1. **task_01_unpacking.py** - Packing and unpacking sequences
2. **task_02_args_kwargs.py** - Working with `*args` and `**kwargs`
3. **task_03_callable_lambda.py** - Functions as arguments and lambdas
4. **task_04_scope.py** - Global, local, and nonlocal variables
5. **task_05_decorators.py** - Decorators and decorator factories

Each task file contains function stubs with detailed docstrings. Read the docstrings carefully and implement the functions.

## Setup

### 1. Fork this repository

Click the "Fork" button at the top right of this repository page.

### 2. Clone your fork

```bash
git clone https://github.com/YOUR_USERNAME/python-functions-scope-decorators-homework.git
cd python-functions-scope-decorators-homework
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Working on the homework

1. Open the files in the `src/` directory
2. Read the docstrings carefully
3. Replace `raise NotImplementedError` with your solution
4. Run tests to verify your solution

All tests will fail at first — that is expected. Your job is to make them pass.

Do **not** modify anything inside `tests/`.

## Running tests

Run all tests:

```bash
pytest
```

Run tests for a specific task:

```bash
pytest tests/test_task_01_unpacking.py
pytest tests/test_task_02_args_kwargs.py
pytest tests/test_task_03_callable_lambda.py
pytest tests/test_task_04_scope.py
pytest tests/test_task_05_decorators.py
```

Run tests with verbose output:

```bash
pytest -v
pytest tests/test_task_01_unpacking.py -v
```

## Submitting your work

### 1. Create a new branch

```bash
git checkout -b solution
```

### 2. Commit your changes

```bash
git add src/
git commit -m "Implement function tasks"
```

### 3. Push to your fork

```bash
git push origin solution
```

### 4. Create a Pull Request

1. Go to your fork on GitHub
2. Click "Pull requests" → "New pull request"
3. Select `base repository: original-repo` and `compare: solution`
4. Click "Create pull request"
5. Add a title and description
6. Submit the pull request

## Requirements

- Python 3.11+
- All tests must pass before submitting

Good luck!

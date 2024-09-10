# 0x03. Unittests and Integration Tests

## Overview

This project covers the process of writing unit tests and integration tests for Python functions and classes. Unit tests check if individual functions return the expected results for a variety of inputs, while integration tests check interactions between different parts of the code.

## Task 0: Parameterize a Unit Test

**`Description`**:

We wrote a unit test for the `utils.access_nested_map` function, which retrieves values from a nested dictionary based on a sequence of keys. The test was parameterized to handle multiple input cases efficiently.

**`Solution`**:

- **File**: `test_utils.py`
- **Tested Function**: `access_nested_map` from `utils.py`

We tested the function with the following inputs:

1. `nested_map={"a": 1}, path=("a",)`: Expected result: `1`
2. `nested_map={"a": {"b": 2}}, path=("a",)`: Expected result: `{"b": 2}`
3. `nested_map={"a": {"b": 2}}, path=("a", "b")`: Expected result: `2`

**`Requirements`**:

- Files interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Python files follow `pycodestyle` style (version 2.5).
- The `@parameterized.expand` decorator was used to test multiple input cases.

**`Example Usage`**:

```bash
python -m unittest test_utils.py
```

## Task 1: Parameterize a Unit Test (Exception Handling)

**`Description`**:

We extended the unit test for the `access_nested_map` function to check that a `KeyError` is raised for invalid paths in the nested map. The test was parameterized to handle multiple input cases where errors are expected.

**`Solution`**:

- **File**: `test_utils.py`
- **Tested Function**: `access_nested_map` from `utils.py`

We tested the function with the following invalid inputs:

1. `nested_map={}, path=("a",)`: Expected result: `KeyError`
2. `nested_map={"a": 1}, path=("a", "b")`: Expected result: `KeyError`

**`Requirements`**:

- Files interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Python files follow `pycodestyle` style (version 2.5).
- The `assertRaises` context manager was used to verify the `KeyError`.

**`Example Usage`**:

```bash
python -m unittest test_utils.py
```

## Task 2: Mock HTTP Calls

**`Description`**:

We extended the `test_utils.py` file to include unit tests for the `get_json` function from `utils.py`. This function retrieves JSON data from a remote URL using HTTP GET requests. Since we don't want to make actual HTTP calls during testing, we mocked the `requests.get` method using `unittest.mock.patch`.

**`Solution`**:

- **File**: `test_utils.py`
- **Tested Function**: `get_json` from `utils.py`

We tested the function with the following inputs:

1. `test_url="http://example.com", test_payload={"payload": True}`
2. `test_url="http://holberton.io", test_payload={"payload": False}`

**`Requirements`**:

- Files interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Python files follow `pycodestyle` style (version 2.5).
- The `requests.get` method was mocked using `unittest.mock.patch`.

**`Example Usage`**:

```bash
python -m unittest test_utils.py
```

## Task 3: Parameterize and Patch

**`Description`**:

We wrote unit tests for the `memoize` decorator from `utils.py`. The `memoize` decorator caches the result of a method after the first call, ensuring that subsequent calls return the cached result without re-executing the method. 

**`Solution`**:

- **File**: `test_utils.py`
- **Tested Function**: `memoize` from `utils.py`

We tested the memoization using the following inputs:

- A `TestClass` with a method `a_method()` that returns `42`.
- The method was decorated with `@memoize` and accessed twice.

**`Requirements`**:

- Files interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Python files follow `pycodestyle` style (version 2.5).
- The `unittest.mock.patch` was used to mock `a_method` and assert it was only called once.

**`Example Usage`**:

```bash
python -m unittest test_utils.py
```

## Task 4: Parameterize and Patch as Decorators

**`Description`**:

We wrote unit tests for the `GithubOrgClient.org` method from `client.py`. This method retrieves data from the GitHub API for a given organization. We used `unittest.mock.patch` to mock the `get_json` method to avoid making actual HTTP calls during testing.

**`Solution`**:

- **File**: `test_client.py`
- **Tested Class**: `GithubOrgClient` from `client.py`

We tested the `org` method with the following inputs:

1. `org_name="google"`
2. `org_name="abc"`

**`Requirements`**:

- Files interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Python files follow `pycodestyle` style (version 2.5).
- The `get_json` method was mocked using `unittest.mock.patch`.

**`Example Usage`**:

```bash
python -m unittest test_client.py
```

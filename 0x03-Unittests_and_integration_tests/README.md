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

## Task 5: Mocking a Property

**`Description`**:

We wrote a unit test for the `GithubOrgClient._public_repos_url` method from `client.py`. This method retrieves the public repositories URL for a given organization. We used `unittest.mock.patch` to mock the `org` property and return a predefined payload with the `repos_url`.

**`Solution`**:

- **File**: `test_client.py`
- **Tested Method**: `_public_repos_url` from `GithubOrgClient` in `client.py`

We mocked the `org` property to return the following payload:

```python
{"repos_url": "https://api.github.com/orgs/mock_org/repos"}
```

## Task 6: More Patching

**`Description`**:

We wrote a unit test for the `GithubOrgClient.public_repos` method from `client.py`. This method retrieves a list of public repositories for a given organization. We used `unittest.mock.patch` to mock both the `get_json` function and the `_public_repos_url` property.

**`Solution`**:

- **File**: `test_client.py`
- **Tested Method**: `public_repos` from `GithubOrgClient` in `client.py`

We mocked `get_json` to return the following payload:

```python
[{"name": "repo1"}, {"name": "repo2"}]
```

## Task 7: Parameterize

**`Description`**:

We wrote a unit test for the `GithubOrgClient.has_license` method from `client.py`. This method checks whether a given repository has a specific license.

**`Solution`**:

- **File**: `test_client.py`
- **Tested Method**: `has_license` from `GithubOrgClient` in `client.py`

We parameterized the test with the following inputs:

1. A repository with the license `my_license` and the expected output is `True`.
2. A repository with a different license (`other_license`) and the expected output is `False`.
3. A repository without a license, with the expected output being `False`.

**`Example Usage`**:

```bash
python -m unittest test_client.py
```

## Task 8: Integration Test with Fixtures

**`Description`**:

We wrote integration tests for the `GithubOrgClient.public_repos` method from `client.py`. These tests ensure that the method returns the expected list of public repositories, both with and without license filtering.

**`Solution`**:

- **File**: `test_client.py`
- **Tested Method**: `public_repos` from `GithubOrgClient` in `client.py`

We used fixtures from `fixtures.py`:

- `org_payload`: Simulated payload for the organization.
- `repos_payload`: Simulated payload for repositories.
- `expected_repos`: The expected repositories list.
- `apache2_repos`: The expected repositories filtered by `apache-2.0` license.

**`Requirements`**:

- The `requests.get` method is mocked using `unittest.mock.patch` to return the payloads from the fixtures.

**`Example Usage`**:

```bash
python -m unittest test_client.py
```

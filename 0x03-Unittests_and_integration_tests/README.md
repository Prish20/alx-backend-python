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

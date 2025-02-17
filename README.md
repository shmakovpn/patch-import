# patch-import

![Tests](https://github.com/shmakovpn/patch-import/actions/workflows/python-package.yml/badge.svg)
[![codecov](https://codecov.io/github/shmakovpn/patch-import/graph/badge.svg?token=744XXMAKOZ)](https://codecov.io/github/shmakovpn/patch-import)
![Mypy](https://github.com/shmakovpn/patch-import/actions/workflows/mypy.yml/badge.svg)
[![pypi](https://img.shields.io/pypi/v/patch-import.svg)](https://pypi.python.org/pypi/patch-import)
[![downloads](https://static.pepy.tech/badge/patch-import/month)](https://pepy.tech/project/patch-import)
[![versions](https://img.shields.io/pypi/pyversions/patch-import.svg)](https://github.com/shmakovpn/patch-import)

Sometimes it is necessary to disable the real import of a Python module and replace the import result with a mock object.

## Installation

```bash
pip install patch-import
```

## Example

```py
import pytest
from patch_import import patch_import


@pytest.fixture
def aiohttp__import_fixture():
    with patch_import('aiohttp') as mocked_aiohttp:
        mocked_aiohttp.__version__ = '3.3.3'
        yield mocked_aiohttp


class TestPatchImport:
    def test_patch_import(self, aiohttp__import_fixture):
        """An example test with patch_import"""
        # patch_import__fixtures.py imports aiohttp which does not present in a project environment
        # thus, we need to disable real import and replace aiohttp for a mock object
        from patch_import.patch_import__fixtures import MyClass  # please look at src/patch_import/patch_import__fixtures.py
        assert MyClass.version() == '3.3.3'
```

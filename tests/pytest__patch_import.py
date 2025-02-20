import pytest
import os
from unittest.mock import Mock
from patch_import import patch_import

real_cwd: str = os.getcwd()  # real cwd


@pytest.fixture
def aiohttp__import_fixture():
    with patch_import('aiohttp') as mocked_aiohttp:
        mocked_aiohttp.__version__ = '3.3.3'
        yield mocked_aiohttp


@pytest.fixture
def os__import_fixture():
    with patch_import('os') as mocked_os:
        yield mocked_os


class TestPatchImport:
    def test_patch_import(self, aiohttp__import_fixture, os__import_fixture):
        """An example test with patch_import"""
        from patch_import.patch_import__fixtures import MyClass
        assert MyClass.version() == '3.3.3'

    def test_patch_import__coverage(self, aiohttp__import_fixture, os__import_fixture):
        """increase coverage"""
        from patch_import.patch_import__fixtures import MyClass
        r = MyClass.cwd()
        assert isinstance(r, Mock)
        assert r != real_cwd

    def test_patch_import__exceptions(self):
        """increase coverage, test exception re-raise"""
        class SomeError(Exception):
            pass

        with pytest.raises(SomeError):
            with patch_import('sys'):
                raise SomeError

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
        from patch_import.patch_import__fixtures import MyClass
        assert MyClass.version() == '3.3.3'

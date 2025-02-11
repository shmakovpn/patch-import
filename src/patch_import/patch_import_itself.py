from typing import Generator
from unittest.mock import Mock
import sys
from contextlib import contextmanager


__all__ = (
    'patch_import',
)


@contextmanager
def patch_import(target: str) -> Generator[Mock, None, None]:
    """
    Example:

    @pytest.fixture
    def aiohttp__import_fixture():
        with patch_import('aiohttp') as mocked_aiohttp:
            yield mocked_aiohttp

    class TestAioHttpApplication:
        def test_inheritance(self, aiohttp__import_fixture):
            from my_module import MyClass  # move imports under test
            # inside my_module aiohttp will be a mock object
            assert MyClass.something()  # some test logic
    """
    old_module = sys.modules.pop(target, None)
    mock_module = Mock()
    sys.modules[target] = mock_module
    try:
        yield mock_module
    except Exception:
        raise
    finally:
        if old_module:
            sys.modules[target] = old_module
        else:
            del sys.modules[target]

import aiohttp  # aiohttp does not present in this project
import os

__all__ = (
    'MyClass',
)


class MyClass:
    @classmethod
    def version(cls):
        """some method that uses aiohttp"""
        return aiohttp.__version__

    @classmethod
    def cwd(self) -> str:
        """increase coverage"""
        return os.getcwd()

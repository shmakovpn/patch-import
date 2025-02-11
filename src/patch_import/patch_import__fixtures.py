import aiohttp  # aiohttp does not present in this project

__all__ = (
    'MyClass',
)


class MyClass:
    @classmethod
    def version(cls):
        """some method that uses aiohttp"""
        return aiohttp.__version__

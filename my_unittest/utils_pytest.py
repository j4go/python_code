import pytest

from utils import to_str


class TestUtils:
    """Test utils.to_str

    pytest class name must start with 'Test'
    pytest method name must start with 'test'

    pytest doc: https://docs.pytest.org/en/latest/
    https://docs.pytest.org/en/latest/getting-started.html#getstarted

    The pytest framework makes it easy to write small tests,
    yet scales to support complex functional testing for applications
    and libraries.
    """

    def test_to_str_bytes(self):
        assert to_str(b'hello') == 'hello'

    def test_to_str_str(self):
        assert to_str('hello') == 'hello'

    def test_to_str_int(self):
        with pytest.raises(TypeError):
            to_str(3)


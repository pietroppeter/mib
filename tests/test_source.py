import pytest

from nobe.source import _cleanup

source_simple_lambda = """
nb.code(lambda: print("hi"))
"""

cleaned_simple_lambda = """
print("hi")
"""

source_simple_decorator = """
@nb.code
def _():
    print("hello")
"""

cleaned_simple_decorator = """
print("hello")
"""

cleanup_test_data = [
    (source_simple_lambda, cleaned_simple_lambda),
    (source_simple_decorator, cleaned_simple_decorator),
]


@pytest.mark.parametrize("source, cleaned", cleanup_test_data)
def test_source_cleanup(source: str, cleaned: str):
    pass

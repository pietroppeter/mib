import inspect
import re
from textwrap import dedent
from typing import Callable


def _cleanup(source):
    # Handle nb.code with lambda
    source = re.sub(r"nb\.code\(lambda: (.*?)\)", r"\1", source)
    # Remove nb.code decorator and any function definition
    source = re.sub(r"@nb\.code\s*\ndef \w+\(\):\n", "", source)
    # Remove indentation using dedent
    return dedent(source).strip()


def getsource(callable: Callable):
    source = inspect.getsource(callable)
    return _cleanup(source)


if __name__ == "__main__":
    # Example usage
    input_text = '@nb.code\ndef example():\n  print("hello")'
    output_text = _cleanup(input_text)
    print(output_text)  # Expected output: print("hello")


# first iteration of this module done with chatgpt: https://chatgpt.com/canvas/shared/67d6687bde4c8191b28ca32421063af6

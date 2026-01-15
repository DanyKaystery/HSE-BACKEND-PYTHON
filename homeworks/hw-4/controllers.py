from typing import Optional


def operation(a: int, b: int) -> Optional[int]:
    if (a is None) or (b is None):
        return None
    return a + b
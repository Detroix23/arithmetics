"""
# Arithmetics: shared.
/src/shared/defaults.py
"""

from typing import Callable 

Real = float | int

FunctionReal = Callable[[float], float]
"""
f: R → R
"""


FunctionReal2 = Callable[[float, float], float]
"""
f: (R×R) → R
"""

__all__: list[str] = ["Real", "FunctionReal", "FunctionReal2"]

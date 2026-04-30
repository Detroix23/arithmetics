"""
# Arithmetics: shared.
/src/shared/defaults.py
"""

from typing import Callable 

import numpy


Real = float | int
FunctionReal = Callable[[float], float]
"""
f: R → R
"""
FunctionReal2 = Callable[[float, float], float]
"""
f: (R×R) → R
"""
IntegerArray = numpy.ndarray[tuple[int], numpy.dtype[numpy.int32]]
UnsignedIntegerArray = numpy.ndarray[tuple[int], numpy.dtype[numpy.uint64]]
RealArray = numpy.ndarray[tuple[int], numpy.dtype[numpy.float64]]

__all__: list[str] = ["Real", "FunctionReal", "FunctionReal2", "IntegerArray"]

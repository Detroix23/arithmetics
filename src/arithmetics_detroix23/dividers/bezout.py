"""
# Arithmetics.
/src/arithmetics_detroix23/dividers/bezout.py

Bézout identity:
_If_  GCD(a, b) | c,
_Then_ ∃(x, y) ∈ ℕ² such as:
```
ax + by = c
```
"""

def particular_from_euclid(remainders: list[int]) -> tuple[int, int]:
	"""
	Finds one solution by steping-back the Euclid algorithm `remainders`.

	These `remainders` can be seen as a table:
	|  a  |  b  |  r  |
	| --- | --- | --- |
	| r1  | r2  | r3  |
	| r2  | r3  | r4  |  

	"""
	...
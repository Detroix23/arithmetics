"""
# Arithmetics.
/src/arithmetics_detroix23/dividers/gcd.py
"""

def euclid(a: int, b: int) -> int:
	"""
	Compute the GCD using euclid algorithm of consecutive euclidean divisions.
	
	Returns **d**, GCD of `a ` and `b`.
	"""
	r1: int = max(a, b)
	r2: int = min(a, b)
	r3: int

	while r2 != 0:
		r3 = r1 % r2
		r1 = r2
		r2 = r3

	return r1

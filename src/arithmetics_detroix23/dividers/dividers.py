"""
# Arithmetics.
/src/arithmetics_detroix23/dividers/dividers.py
"""

def get_list(n: int) -> list[int]:
	"""
	Returns a list of positive dividers of `n`. Exclude 1 and `n`.
	"""
	dividers: list[int] = []

	for d in range(2, n):
		if n % d == 0:
			dividers.append(d)

	return dividers

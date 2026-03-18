"""
# Arithmetics.
/src/arithmetics_detroix23/consecutive_signed_sums/forms.py
"""

import pprint

def binary_combinations(
	n: int, 
) -> list[list[bool]]:
	"""
	All possible combinations of `n` binary variables. 
	"""
	iterations: int = 0
	combinations: list[list[bool]] = [[True], [False]]
	clones: list[list[bool]] = []

	while iterations < n - 1:
		for selector in range(len(combinations)):
			current: list[bool] = combinations[selector]
			clone: list[bool] = current[:]
			
			current.append(True)
			clone.append(False)
			clones.append(clone)

		for clone in clones:
			combinations.append(clone)
		clones = []
		iterations += 1

	return combinations

def all_combinations(n: int) -> dict[int, list[list[bool]]]:
	"""
	Go through all combinations of sums up to `n` numbers.
	"""
	found: dict[int, list[list[bool]]] = {}

	for size in range(n):
		signs_combinations = binary_combinations(size)

		for signs in signs_combinations:
			result: int = 0
			for i, sign in enumerate(signs, 1):
				result += (1 if sign else -1) * i
			
			if result in found.keys():
				found[result].append(signs)
			else:
				found[result] = [signs]

	return found

def format_signs(bits: list[bool]) -> str:
	"""
	Format a `list` of `bool` to [-1](False) and [1](True)
	"""
	return " + ".join([(f"(+1)✕{i}" if sign else f"(-1)✕{i}") for i, sign in enumerate(bits, 1)])

def format_all_combinations(result: dict[int, list[list[bool]]]) -> str:
	lines: list[str] = []
	for integer, combinations in result.items():
		lines.append(f"• {integer}")
		for combination in combinations:
			lines.append(f"  = {format_signs(combination)}")

	return "\n".join(lines)

def main() -> None:
	"""
	Main testing for consecutive signed sums.
	"""
	print("## Combinations.")
	b1 = binary_combinations(1)
	b2 = binary_combinations(2)
	b3 = binary_combinations(3)
	b4 = binary_combinations(4)

	print(b1, len(b1))
	print(b2, len(b2))
	print(b3, len(b3))
	print(b4, len(b4))

	print("## Forms.")
	f = all_combinations(5)
	print(format_all_combinations(f))

	



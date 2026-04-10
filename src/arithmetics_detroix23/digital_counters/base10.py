"""
# Digital counters.
/src/digital_counters_detroix23/base10.py
"""

def count_digits(number: int) -> dict[int, int]:
	"""
	Count digits of a number. Returns a dictionary like `digit: count`.
	"""
	string: str = str(number)
	digits: dict[int, int] = { i: 0 for i in range(10) }
	for digit in string:
		try:
			digits[int(digit)] += 1 
		except KeyError:
			print(f"(!) decimal.count_digits(number={number}) Unknown character `{digit}`.")

	return digits

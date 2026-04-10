"""
# Digital counters.
/src/digital_counters_detroix23/romans.py
"""

DIGITS: list[int] = [1000, 500, 100, 50, 10, 5, 1, 0]
REPRESENTATION: dict[int, str] = {
	1000: "M",
	500: "D",
	100: "C",
	50: "L",
	10: "X",
	5: "V",
	1: "I",
	0: "0",
}

class RomanNumeral:
	"""
	# `RomanNumeral`.
	Written with digits:
	- _0_ (0),
	- _I_ (1), 
	- _V_ (5),
	- _X_ (10),
	- _L_ (50),
	- _C_ (100),
	- _D_ (500),
	- _M_ (1000).
	"""
	_number: int
	_digits: dict[int, int]

	def __init__(self, number: int) -> None:
		self._number = number
		self._digits = { digit: 0 for digit in DIGITS }
		
		self.encode()

	def get_number(self) -> int:
		return self._number
	
	def get_digits(self) -> dict[int, int]:
		return self._digits
 
	def __str__(self) -> str:
		string: str = ""
		for digit in DIGITS:
			string += REPRESENTATION[digit] * self._digits[digit]

		return string

	def __repr__(self) -> str:
		return f"RomanNumeral(number={self._number}, digits={self._digits})"

	def encode(self) -> dict[int, int]:
		"""
		Encode, using a greedy strategy, the `number` into roman `digits`. Return these digits.
		"""
		number: int = self._number
		digits_index: int = 0

		while number > 0 and digits_index < len(DIGITS):
			digit: int = DIGITS[digits_index]
			
			while number - digit >= 0:
				number -= digit
				self._digits[digit] += 1

			digits_index += 1

		return self._digits
	
"""
# Arithmetics.
/src/conway_sequence/sequence.py
"""


class ConwaySequence:
	"""
	# `ConwaySequence` step compute and saving.
	"""
	sample_count: int
	history: list[int]
	i: int

	def __init__(
		self, 
		sample_count: int,
		start_value: int,
	) -> None:
		"""
		Initialize the start of the `ConwaySequence`.
		"""
		self.sample_count = sample_count
		self.history = [0 for _ in range(self.sample_count)]
		self.history[0] = start_value
		self.i = 1

	def complete(self) -> list[int]:
		"""
		Recurse the `ConwaySequence` `sample_count` times.
		"""
		compressed: int
		while self.i < self.sample_count:
			compressed = compress(self.history[self.i - 1])
			self.history[self.i] = compressed 
			self.i += 1
	
		return self.history


def compress(number: int) -> int:
	"""
	Transform the `number` by _looking-and-saying_ sequences of identical digits.

	Concatenate for each number the repetition count and the number.

	**Exemple:**

	n = 22311199
	> two 2s, one 3, three 1s, two 9  

	n' = 22133129
	```
	"""
	repeated: str = ""
	count: int = 0
	new: str = ""

	for digit in str(number):
		if digit == repeated:
			count += 1
		else:
			new += f"{count}{repeated}"
			repeated = digit
			count = 1
	
	if count > 0:
		new += f"{count}{repeated}"

	return int(new)

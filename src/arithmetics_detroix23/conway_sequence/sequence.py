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

	def length_average(self) -> float:
		"""
		Average length of all values **l_n**.
		"""
		length_sum: int = 0
		for value in self.history:
			length_sum += len(str(value))

		return length_sum / len(self.history)

	def digit_count(self) -> dict[str, tuple[int, float]]:
		"""
		Returns a dictionary:
		- keys: `str`, digit ("total" special case);
		- values: `tuple[int, float]`, (count, frequency);
		"""
		counts: dict[str, int] = {
			"1": 0,
			"2": 0,
			"3": 0,
			"total": 0
		}

		for number in self.history:
			string = str(number)
			for digit in string:
				if digit in counts.keys():
					counts[digit] += 1
				else:
					counts[digit] = 0
			counts["total"] += len(string)
					
		frequency: dict[str, float] = {
			digit: count / counts["total"] for digit, count in counts.items()
		}

		concatenated = {digit: (counts[digit], frequency[digit]) for digit in counts.keys()}
		return concatenated


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

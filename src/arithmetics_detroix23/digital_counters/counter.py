"""
# Digital counters.
/src/digital_counters_detroix23/decimal.py
"""

from matplotlib import pyplot, ticker

from arithmetics_detroix23.shared import base10

def counter_numerical_raw(start: int, stop: int) -> dict[int, int]:
	"""
	For each number between `start` and `stop` (inclusive), sum the digits count.
	"""
	total: dict[int, int] = { i: 0 for i in range(10) }

	for number in range(start, stop + 1):
		digits: dict[int, int] = base10.count_digits(number)
		for digit, count in digits.items():
			total[digit] += count
	
	return total

def plot_raw(start: int, stop: int) -> None:
	count: dict[int, int] = counter_numerical_raw(start, stop)
	figure, axes = pyplot.subplots()
	
	axes.bar(tuple(count.keys()), tuple(count.values()))
	
	axes.set_title(f"Digits for a digital clock from {start} to {stop}.")
	axes.xaxis.set_major_locator(ticker.MultipleLocator(1))
	axes.xaxis.set_label_text("Digit `n`.")

	axes.yaxis.set_label_text("Occurrences `q`.")

	pyplot.show()
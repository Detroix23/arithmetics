"""
# Arithmetics.
/src/conway_sequence/tests.py
"""

import numpy
from matplotlib import pyplot
import pprint

from arithmetics_detroix23.shared.defaults import IntegerArray, RealArray
from arithmetics_detroix23.conway_sequence import sequence

def compress1() -> None:
	print("\n## Tests: Conway compress 1.")

	assert sequence.compress(22311199) == 22133129
	assert sequence.compress(10020) == 11201210
	assert sequence.compress(111221) == 312211
	assert sequence.compress(22) == 22

	
def sequence1() -> None:
	print("\n## Tests: Conway sequence 1.")
	
	l20 = sequence.ConwaySequence(20, 1)

	print(f"l20: \n{l20.complete()}")

	print("l20.counts: ")
	pprint.pprint(l20.digit_count())

def count_over_start1() -> None:
	print("\n## Tests: Count over start 1.")

	sample_count: int = 20
	upper_start: int = 100
	counts1: IntegerArray = numpy.zeros((upper_start - 1,), dtype=numpy.int32)
	frequencies1: RealArray = numpy.zeros((upper_start,), dtype=numpy.float64)
	length_averages: RealArray = numpy.zeros((upper_start - 1,), dtype=numpy.float64)

	for l_0 in range(1, upper_start):
		l_n = sequence.ConwaySequence(sample_count, l_0)
		l_n.complete()
		count: dict[str, tuple[int, float]] = l_n.digit_count()

		counts1[l_0 - 1] = count["1"][0]
		frequencies1[l_0 - 1] = count["1"][1]
		length_averages[l_0 - 1] = l_n.length_average()

	print(f"Last result for l0={upper_start - 1}:")
	pprint.pprint(count)

	(figure, axes) = pyplot.subplots()
	axes.plot(counts1)
	axes.plot(frequencies1)
	axes.plot(length_averages)
	
	axes.set_title("Digit statistics on Conway sequence.")
	axes.set_xlabel("l_0")
	axes.set_ylabel("y")
	axes.legend([
		"Count 1",
		"Frequency 1",
		"Length average"
	])

	pyplot.show()

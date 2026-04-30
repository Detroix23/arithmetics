"""
# Arithmetics.
/src/conway_sequence/tests.py
"""

from arithmetics_detroix23.conway_sequence import sequence

def compress1() -> None:
	print("Tests: Conway compress 1.")

	assert sequence.compress(22311199) == 22133129
	assert sequence.compress(10020) == 11201210
	assert sequence.compress(111221) == 312211
	assert sequence.compress(22) == 22

	l20 = sequence.ConwaySequence(20, 1)

	print(f"l20: \n{l20.complete()}")

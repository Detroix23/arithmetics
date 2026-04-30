"""
# Arithmetics.
/src/arithmetics_detroix23/__main__.py
"""

from arithmetics_detroix23 import (
	digital_counters, 
	consecutive_signed_sums,
	predators_prays,
	dividers,
	conway_sequence,
)

def main() -> None:
	"""
	Main entry point to test proposed arithmetic problems.
	"""
	
	# Digital counters.
	# digital_counters.tests.main()

	# Consecutive signed sums.
	# consecutive_signed_sums.forms.main()

	# Prays and predators.
	# predators_prays.tests.capes1()

	# Dividers, GCP, primes.
	#dividers.tests.euclid_result1()
	#dividers.tests.gcd_scatter()
	#dividers.tests.gcd_study1()

	# Conway sequence.
	conway_sequence.tests.compress1()

main()

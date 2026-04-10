"""
# Digital counters.
/src/digital_counters_detroix23/__main__.py

Simulate counters, in base 10 and in roman numbers.

Try to find the best combination for the minimal counter.
"""

from arithmetics_detroix23.digital_counters import romans, counter

def main() -> None:
	"""
	Main entry point for the digital counters simulations.
	"""
	print("# Digital counters.")

	counter1()

def romans1() -> None:
	print("## Test: romans 1.")

	r1 = romans.RomanNumeral(1)
	print(r1)
	r2 = romans.RomanNumeral(3)
	print(r2)
	r3 = romans.RomanNumeral(5)
	print(r3)
	r4 = romans.RomanNumeral(43)
	print(r4)
	r5 = romans.RomanNumeral(123)
	print(r5)

def counter1() -> None:
	print("## Test: counter 1.")

	c1: dict[int, int] = counter.counter_numerical_raw(1, 1)
	c2: dict[int, int] = counter.counter_numerical_raw(1, 10)
	c3: dict[int, int] = counter.counter_numerical_raw(0, 10)
	
	counter.plot_raw(1, 32)

	counter.plot_raw(1, 999)


if __name__ == "__main__":
	main()

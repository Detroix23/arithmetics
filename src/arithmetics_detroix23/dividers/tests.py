"""
# Arithmetics.
/src/arithmetics_detroix23/dividers/tests.py
"""

import numpy
from matplotlib import pyplot

from arithmetics_detroix23.shared.defaults import IntegerArray, RealArray
from arithmetics_detroix23.dividers import gcd

def euclid_result1() -> None:
	print("\n## Test: GCD euclid method 1.")
	print(gcd.euclid(5, 3))
	print(gcd.euclid(3, 5))
	print(gcd.euclid(15, 3))
	print(gcd.euclid(24, 6))
	print(gcd.euclid(9, 6))
	print(gcd.euclid(3500, 31230))

def gcd_study1() -> None:
	print("\n## Test: GCD study 1.")
	samples = 200
	averages: RealArray = numpy.zeros((samples,), dtype=numpy.float64)
	count1: IntegerArray = numpy.zeros((samples,), dtype=numpy.int32)
	proportion1: RealArray = numpy.zeros((samples,), dtype=numpy.float64)

	for size in range(1, samples + 1):
		gcd_results: IntegerArray = numpy.zeros((size * size,), dtype=numpy.int32)

		for j in range(size):
			for i in range(size):
				x: int = i
				y: int = j
				gcd_results[j * (size) + i] = abs(gcd.euclid(x, y))

		gcd_average = numpy.sum(gcd_results) / len(gcd_results)
		averages[size - 1] = gcd_average
		
		gcd_1_count = 0
		for d in gcd_results:
			if d == 1:
				gcd_1_count += 1
		gcd_1_proportion = gcd_1_count / (size * size)
		count1[size - 1] = gcd_1_count
		proportion1[size - 1] = gcd_1_proportion

		if size == samples:
			print("### Parameters (last iteration):")
			print(f"- `size` s = {size} => area A = {size * size}")
			print(f"GCD average d = {gcd_average}")
			print(f"GCD=1 count: d1 = {gcd_1_count}.")
			print(f"GCD=1 proportion: d1/A = {gcd_1_proportion}")

	(figure, axes) = pyplot.subplots()
	axes.set_title("""GCD study 1.
Average, count and proportion d=1.""")

	axes.plot(averages)
	# axes.plot(count1)
	axes.plot(proportion1)
	
	axes.legend([
		"Average of d",
		# "Count d=1",
		"Proportion d=1",
	])
	axes.set_xlabel("sample size")
	axes.set_ylabel("result")

	pyplot.show()


def gcd_scatter() -> None:
	print("\n## Test: GCD plane study and scatter.")

	size: int = 100
	xs: IntegerArray = numpy.zeros((size * size,), dtype=numpy.int32)
	ys: IntegerArray = numpy.zeros((size * size,), dtype=numpy.int32)
	ss: IntegerArray = numpy.zeros((size * size,), dtype=numpy.int32)

	for j in range(size):
		for i in range(size):
			x: int = i
			y: int = j

			xs[j * (size) + i] = x
			ys[j * (size) + i] = y
			ss[j * (size) + i] = abs(gcd.euclid(x, y))

	gcd_average = numpy.sum(ss) / len(ss)
	print(f"GCD average d = {gcd_average}")

	(figure, axes) = pyplot.subplots()
	
	axes.scatter(xs, ys, ss)

	axes.set_title("""GCD scatter. 
Radius is the GCD(a, b).""")
	axes.set_xlabel("a")
	axes.set_ylabel("b")
	
	pyplot.show()

"""
# Arithmetics: predators and prays.
/src/predators_prays/simulation.py
"""

import numpy

from arithmetics_detroix23.shared.defaults import *

Int = numpy.int64

class Simulation:
	"""
	# Predators and pray `Simulation`.
	Based on the following recurrence **(R)**:
	```
	∀n ∈ N,
	⎧ x(n+1) = f(x(n), y(n))  
	⎨    
	⎩ y(n+1) = g(x(n), y(n))  
	```

	"""
	n: int
	maximum: int
	f: FunctionReal2
	g: FunctionReal2
	xs: numpy.typing.NDArray[Int]
	ys: numpy.typing.NDArray[Int]
	
	def __init__(
		self, 
		f: FunctionReal2, 
		g: FunctionReal2,
		x0: Real,
		y0: Real,
		maximum: int,
	) -> None:
		self.n = 0
		self.maximum = maximum
		self.f = f
		self.g = g
		self.xs = numpy.zeros((maximum, 1), dtype=Int)
		self.xs[0] = x0
		self.ys = numpy.zeros((maximum, 1), dtype=Int)
		self.ys[0] = y0

	def step(self) -> tuple[float, float]:
		"""
		Advance 1 tick, step in the simulation, by applying the recurrence **(R)**.
		"""
		if self.n >= self.maximum - 1:
			print(f"(!) Simulation reached `n` maximum ({self.maximum}).")
			return (self.xs[self.n], self.ys[self.n])

		x_next: float = (self.f)(self.xs[self.n], self.ys[self.n])
		y_next: float = (self.g)(self.xs[self.n], self.ys[self.n])
		self.xs[self.n + 1] = x_next
		self.ys[self.n + 1] = y_next

		self.n += 1
		
		return (x_next, y_next)
	
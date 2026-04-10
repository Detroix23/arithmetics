"""
# Arithmetics: predators and prays.
/src/predators_prays/tests.py
"""

from matplotlib import pyplot

from arithmetics_detroix23.predators_prays import simulation

def capes1() -> None:
	a = 1.0
	s = simulation.Simulation(
		f=lambda x, y: a * x - y * y,
		g=lambda x, y: a * y - x * x,
		x0=1,
		y0=2,
		maximum=100,
	)

	for _ in range(99):
		s.step()

	(figure, axes) = pyplot.subplots()

	axes.plot(s.xs, s.ys, "-o")

	pyplot.show()

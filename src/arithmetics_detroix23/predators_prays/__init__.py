"""
# Arithmetics: predators and prays.
/src/predators_prays/__init__.py

Evolution of a population of _predators_ x(n) that eat _prays_ y(n).

Source: _CAPES_ 2024 Part 1. 

Model:  
∀n ∈ N,  
⎧ x(n+1) = f(x(n), y(n))  
⎨   
⎩ y(n+1) = g(y(n), x(n))   
 
Example:  
⎧ x(n+1) = x(n) - α × y(n)  
⎨   
⎩ y(n+1) = y(n) + α × x(n)  
"""

from . import tests

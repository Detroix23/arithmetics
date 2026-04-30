"""
# Arithmetics: shared.
/src/shared/cli.py
"""

from arithmetics_detroix23 import (
	digital_counters, 
	consecutive_signed_sums,
	predators_prays,
	dividers,
	conway_sequence,
)

HELP_MESSAGE: str = """
## Help.
```bash
py __main__.py <script>
```

**Arguments**:
`script`:
- `dg`;
- `css`;
- `pp`;
- `gcd`;
- `cs`;
"""

def run_with_arguments(arguments: list[str]) -> None:	
	"""
	Execute the request script.
	"""
	print("# Arithmetics.")

	if len(arguments) <= 1:
		print("Missing <script> at position 1.")
		print(HELP_MESSAGE)

	elif arguments[1] in {"dg", "counters"}:
		digital_counters.tests.main()

	elif arguments[1] in {"css", "sums"}:
		consecutive_signed_sums.forms.main()

	elif arguments[1] in {"pp", "predators", "preys"}:
		predators_prays.tests.capes1()

	elif arguments[1] in {"gcd", "dividers"}:
		dividers.tests.euclid_result1()
		dividers.tests.gcd_scatter()
		dividers.tests.gcd_study1()

	elif arguments[1] in {"cs", "conway"}:
		conway_sequence.tests.compress1()
		conway_sequence.tests.sequence1
		conway_sequence.tests.count_over_start1()

	else:
		print("Incorrect <script> at position 1.")
		print(HELP_MESSAGE)

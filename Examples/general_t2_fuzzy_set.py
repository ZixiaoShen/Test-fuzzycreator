"""This module provides examples of coding with general type-2 fuzzy sets."""
from decimal import Decimal
from fuzzycreator import global_settings as gs

from fuzzycreator.membership_functions.triangular import Triangular
from fuzzycreator.membership_functions.trapezoidal import Trapezoidal
from fuzzycreator.membership_functions.gaussian import Gaussian
from fuzzycreator.fuzzy_sets.general_t2_fuzzy_set import GeneralT2FuzzySet

from fuzzycreator import visualisations

gs.global_uod = (0, 20)
gs.global_x_disc = 201
gs.global_zlevel_disc = 4   # 4 zSlices

# The upper and lower membership functions may be given in any order
A = GeneralT2FuzzySet(Triangular(0, 2, 4), Triangular(1, 2, 3, 0.8))
B = GeneralT2FuzzySet(Trapezoidal(3, 5, 6, 8, 0.8), Trapezoidal(2, 4, 7, 9))
C = GeneralT2FuzzySet(Gaussian(13, 1), Gaussian(13, 0.5, 0.8))
D = GeneralT2FuzzySet(Gaussian(15, 1), Gaussian(16, 1))

print(A.calculate_membership(Decimal('0.5'), Decimal('0.25')))
print(A.calculate_secondary_membership(Decimal('3.5'), Decimal('0.5')))


visualisations.plot_sets((A, B, C, D))

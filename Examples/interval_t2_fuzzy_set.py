"""This module provides examples of coding with interval type-2 fuzzy sets."""

from decimal import Decimal

from fuzzycreator.membership_functions.triangular import Triangular
from fuzzycreator.membership_functions.trapezoidal import Trapezoidal
from fuzzycreator.membership_functions.gaussian import Gaussian
from fuzzycreator.fuzzy_sets.interval_t2_fuzzy_set import IntervalT2FuzzySet
from fuzzycreator.measures import similarity_it2
from fuzzycreator.measures import distance_it2

from fuzzycreator import global_settings as gs

from fuzzycreator import visualisations

gs.global_uod = (0, 20)
gs.global_x_disc = 201

A = IntervalT2FuzzySet(Triangular(0, 2, 4), Triangular(1, 2, 3, 0.8))
B = IntervalT2FuzzySet(Trapezoidal(2, 4, 7, 9), Trapezoidal(3, 5, 6, 8, 0.8))
C = IntervalT2FuzzySet(Gaussian(13, 1), Gaussian(13, 0.5, 0.8))
D = IntervalT2FuzzySet(Gaussian(15, 1), Gaussian(16, 1))


print(A.calculate_membership(Decimal('0.5')))
print(A.calculate_alpha_cut_upper(Decimal('0.5')))
print(A.calculate_alpha_cut_lower(Decimal('0.5')))
print(A.calculate_centre_of_sets())
print(A.calculate_overall_centre_of_sets())

visualisations.plot_sets((A, B, C, D))

print('s(A, B) =', similarity_it2.jaccard(A, B))
print('s(C, D) =', similarity_it2.jaccard(C, D))

print('d(A, B) =', distance_it2.mcculloch(A, B))
print('d(B, A) =', distance_it2.mcculloch(B, A))

print('d(C, D) =', distance_it2.mcculloch(C, D))
print('d(D, C) =', distance_it2.mcculloch(D, C))

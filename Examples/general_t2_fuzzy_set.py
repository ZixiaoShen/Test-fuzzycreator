"""This module provides examples of coding with general type-2 fuzzy sets."""
from decimal import Decimal
from fuzzycreator import global_settings as gs

from fuzzycreator.membership_functions.triangular import Triangular
from fuzzycreator.membership_functions.trapezoidal import Trapezoidal
from fuzzycreator.membership_functions.gaussian import Gaussian
from fuzzycreator.fuzzy_sets.general_t2_fuzzy_set import GeneralT2FuzzySet

from fuzzycreator.measures import similarity_gt2
from fuzzycreator.measures import distance_gt2

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
print(A.calculate_alpha_cut_upper(Decimal('0.5'), Decimal('0.25')))
print(A.calculate_alpha_cut_lower(Decimal('0.5'), Decimal('0.25')))

cos = A.calculate_centre_of_sets()
for z in sorted(cos.keys()):
    print('\tz =', z, cos[z])
print('Centre of type reduced set of A:\n\t')
print(A.calculate_overall_centre_of_sets())

visualisations.plot_sets((A, B, C, D))

print('Demonstrate measuring similarity')
print('s(A, B) =', similarity_gt2.jaccard(A, B))
print('s(C, D) =', similarity_gt2.jaccard(C, D))

print('Demonstrate measuring distance')
print('d(A, B) =', distance_gt2.mcculloch(A, B))
print('d(C, D) =', distance_gt2.mcculloch(C, D))

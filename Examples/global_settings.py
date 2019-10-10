from decimal import Decimal
from fuzzycreator.membership_functions.triangular import Triangular
from fuzzycreator.membership_functions.trapezoidal import Trapezoidal
from fuzzycreator.membership_functions.gaussian import Gaussian
from fuzzycreator.fuzzy_sets.fuzzy_set import FuzzySet

from fuzzycreator.fuzzy_sets.interval_t2_fuzzy_set import IntervalT2FuzzySet
from fuzzycreator.fuzzy_sets.general_t2_fuzzy_set import GeneralT2FuzzySet

from fuzzycreator.measures import similarity_t1
from fuzzycreator.measures import distance_t1

from fuzzycreator import global_settings as gs

from fuzzycreator import visualisations

gs.global_uod = (0, 10)
A = FuzzySet(Triangular(0, 2, 4))
B = FuzzySet(Trapezoidal(3, 5, 7, 9))
C = FuzzySet(Gaussian(10, 1))

visualisations.plot_sets((A, B, C))
gs.global_uod = (0, 15)
visualisations.plot_sets((A, B, C))
C.uod = [0, 15]
visualisations.plot_sets((A, B, C))

gs.global_uod = (0, 10)
C.uod = (0, 10)

gs.global_x_disc = 11
print('global_x_disc = 11:')
print('\ts(B, C) =', similarity_t1.jaccard(B, C))
print('\tCentroid of C =', C.calculate_centroid())

gs.global_x_disc = 101
print('global_x_disc = 101:')
print('\ts(B, C) =', similarity_t1.jaccard(B, C))
print('\tCentroid of C =', C.calculate_centroid())

"""Demonstrate effects of changing the global_alpha_disc"""
gs.global_alpha_disc = 10
print('global_alpha_disc = 10:')
print('\td(B, C) =', distance_t1.chaudhuri_rosenfeld(B, C))

gs.global_alpha_disc = 20
print('global_alpha_disc = 20:')
print('\td(B, C) =', distance_t1.chaudhuri_rosenfeld(B, C))
B.plot_set()

D = IntervalT2FuzzySet(Triangular(3, 5, 7), Triangular(4, 5, 6))
E = GeneralT2FuzzySet(Gaussian(8, 1), Gaussian(8, 0.5))
visualisations.plot_sets((A, D, E))

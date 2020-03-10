from decimal import Decimal
from fuzzycreator.membership_functions.triangular import Triangular
from fuzzycreator.membership_functions.trapezoidal import Trapezoidal
from fuzzycreator.membership_functions.gaussian import Gaussian
from fuzzycreator.fuzzy_sets.fuzzy_set import FuzzySet

from fuzzycreator.measures import similarity_t1
from fuzzycreator.measures import distance_t1

from fuzzycreator import global_settings as gs
from fuzzycreator import visualisations


A = FuzzySet(Triangular(0, 2, 4))
B = FuzzySet(Trapezoidal(3, 5, 7, 9))
C = FuzzySet(Gaussian(5, 1))


# calculations
print(A.calculate_membership(Decimal('3.5')))
print(A.calculate_alpha_cut(Decimal('0.5')))
print(A.calculate_centroid())


gs.global_x_disc = 101
print('s(B, C) =', similarity_t1.jaccard(B, C))


gs.global_alpha_disc = 20
print('d(A, C) =', distance_t1.chaudhuri_rosenfeld(B, C))

visualisations.plot_sets((A, B, C))

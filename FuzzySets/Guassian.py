from fuzzycreator.membership_functions.triangular import Triangular
from fuzzycreator.membership_functions.gaussian import Gaussian
from fuzzycreator.fuzzy_sets.fuzzy_set import FuzzySet
from fuzzycreator import visualisations
from fuzzycreator import global_settings as gs
from fuzzycreator.measures import entropy_t1
from fuzzycreator.measures import inclusion_t1
from fuzzycreator.measures import compatibility_t1


gs.global_uod = (0, 1)
A = FuzzySet(Triangular(0, 0.23, 0.4))
B = FuzzySet(Gaussian(0.34, 0.1))
C = FuzzySet(Gaussian(0.53, 0.14))

visualisations.plot_sets((A, B, C))

print(entropy_t1.kosko(A))
print(entropy_t1.kosko(B))
print(entropy_t1.kosko(C))

print(inclusion_t1.sanchez(A, B))
print(inclusion_t1.sanchez(A, C))
print(inclusion_t1.sanchez(B, C))

print(compatibility_t1.compatibility(A, B))
print(compatibility_t1.compatibility(B, C))
print(compatibility_t1.compatibility(A, C))

# A.plot_set()
# C.plot_set()

from fuzzycreator.membership_functions.triangular import Triangular
from fuzzycreator.membership_functions.gaussian import Gaussian

from fuzzycreator.fuzzy_sets.fuzzy_set import FuzzySet
from fuzzycreator import visualisations
from fuzzycreator import global_settings as gs

gs.global_uod = (0, 1)
A = FuzzySet(Triangular(0, 0.23, 0.4))
C = FuzzySet(Gaussian(0.53, 0.14))

visualisations.plot_sets((A, C))

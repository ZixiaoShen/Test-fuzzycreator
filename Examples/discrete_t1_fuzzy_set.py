from decimal import Decimal

from fuzzycreator.fuzzy_sets.discrete_t1_fuzzy_set import DiscreteT1FuzzySet
from fuzzycreator.measures import similarity_t1
from fuzzycreator import visualisations

A_points = {1: Decimal('0.25'), 2: 1, 3: Decimal('0.25')}
B_points = {2: Decimal('0.33'), 3: Decimal('0.66'), 4: Decimal('0.33')}

A = DiscreteT1FuzzySet(A_points)
B = DiscreteT1FuzzySet(B_points)

visualisations.plot_sets((A, B))

print(A.calculate_membership(1))
print(A.calculate_alpha_cut(Decimal('0.25')))
print(A.calculate_centroid())

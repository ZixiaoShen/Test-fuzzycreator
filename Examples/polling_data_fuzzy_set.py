
import numpy as np

from fuzzycreator import generate_fuzzy_sets
from fuzzycreator import visualisations


def create_fuzzy_set_from_data(d):
    """Plot fuzzy sets generated from data given by load_data()."""
    fuzzy_sets = [generate_fuzzy_sets.generate_polling_t1_fuzzy_set(d)]
    visualisations.plot_sets(fuzzy_sets)


def create_t2_fuzzy_set_from_data(d):
    print('Building type-2 fuzzy set')
    fs = generate_fuzzy_sets.generate_polling_t2_fuzzy_set(d)
    print('Building 3-dimensional plot')
    fs.plot_set_3d()
    print('Building 2-dimensional plot')
    fs.plot_set()


def bimodal_distribution_example():
    """Show polling and Gaussian fuzzy sets based on bi-modal data."""
    d1 = list(np.random.normal(2, 1, 1000))
    d2 = list(np.random.normal(7, 1, 1000))
    d1.extend(d2)
    d1 = [round(i, 1) for i in d1]
    fs = generate_fuzzy_sets.generate_polling_t1_fuzzy_set(d1)
    fs.plot_set()
    fs = generate_fuzzy_sets.generate_polling_t1_fuzzy_set(d1)
    fs.plot_set()


d1 = list(np.random.normal(5, 1, 1000))
d2 = list(np.random.normal(5, 0.5, 1000))
d3 = list(np.random.normal(5, 0.25, 1000))
d1 = [round(i, 1) for i in d1]
d2 = [round(i, 1) for i in d2]
d3 = [round(i, 1) for i in d3]

create_fuzzy_set_from_data(d1)
create_t2_fuzzy_set_from_data([d1, d2, d3])
bimodal_distribution_example()

import numpy as np

from fuzzycreator import generate_fuzzy_sets
from fuzzycreator import global_settings as gs


gs.global_uod = [0, 15]
gs.global_x_disc = 1001
gs.global_zlevel_disc = 3


def generate_data(mean, std_dev=1):
    """Generate normally distributed interval data around the given mean."""
    d1 = list(np.random.normal(mean, std_dev, 100))
    d2 = list(np.random.normal(mean, std_dev, 100))
    d1 = [round(i, 1) for i in d1]
    d2 = [round(i, 1) for i in d2]
    return [(min(d1[i], d2[i]), max(d1[i], d2[i])) for i in range(100)]


def create_fuzzy_set_from_data():
    """Plot fuzzy sets from generated data."""
    mean = np.random.random_integers(0, 10)
    fs = generate_fuzzy_sets.generate_iaa_t1_fuzzy_set(generate_data(mean))
    fs.plot_set()


def create_t2_fuzzy_set_from_data():
    mean = np.random.random_integers(0, 10)
    data = [generate_data(mean, 1),
            generate_data(mean, 0.5),
            generate_data(mean, 0.25)]
    print('..Building type-2 fuzzy set')
    fs = generate_fuzzy_sets.generate_iaa_t2_fuzzy_set(data)
    print('..Plotting 3-dimensional model')
    fs.plot_set_3d()
    print('..Plotting 2-dimensional model')
    fs.plot_set()


create_fuzzy_set_from_data()
create_t2_fuzzy_set_from_data()

import matplotlib.pyplot as plt

from preprocess import preprocess
from utils.luigi_utils import luigi_task


@luigi_task(inputs=preprocess, no_output=True)
def display(series):
    plt.hist(series)
    plt.show()

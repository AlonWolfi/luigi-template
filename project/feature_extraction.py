import numpy as np
import pandas as pd

from utils.luigi_utils import luigi_task


@luigi_task(inputs=None, sample_frac=0.01)
def feature_extraction():
    return pd.Series(
        np.arange(10000)
    )

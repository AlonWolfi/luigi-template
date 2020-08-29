from feature_extraction import feature_extraction
from utils.luigi_utils import luigi_task


@luigi_task(inputs=[feature_extraction])
def preprocess(feature):
    print(feature)
    return feature ** 2

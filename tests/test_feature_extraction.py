from unittest import TestCase

from pandas.util.testing import assert_series_equal

from project.feature_extraction import feature_extraction


class Test(TestCase):
    def test_feature_extraction(self):
        output, output_test = feature_extraction.test()
        assert_series_equal(output, output_test)

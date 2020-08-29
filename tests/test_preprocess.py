from unittest import TestCase

from pandas.util.testing import assert_series_equal

from project.preprocess import preprocess


class Test(TestCase):
    def test_preprocess(self):
        output, output_test = preprocess.test()
        assert_series_equal(output, output_test)

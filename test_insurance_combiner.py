import unittest
from insurance_combiner import InsuranceCombiner
from api_wrappers.api_1 import Api1Wrapper
from api_wrappers.api_2 import Api2Wrapper
from api_wrappers.api_3 import Api3Wrapper
from stubs import *
from mock import patch

class TestInsuranceCombiner(unittest.TestCase):

    def setUp(self):
        self.combiner = InsuranceCombiner('key1', 'key2', 'key3')

    def test_get_plan_averages_pass(self):
        plan_averages = self.combiner.get_plan_averages('123')
        self.assertEqual(plan_averages,
            {'deductible': 1066, 'stop_loss': 11000, 'oop_max': 5666})

    @patch('api_wrappers.api_1.Api1Wrapper.insurance_plan_summary', new=bad_response)
    @patch('api_wrappers.api_2.Api2Wrapper.insurance_plan_summary', new=bad_response)
    @patch('api_wrappers.api_3.Api3Wrapper.insurance_plan_summary', new=bad_response)
    def test_get_plan_averages_all_bad_responses(self):
        plan_averages = self.combiner.get_plan_averages('123')
        self.assertEqual(plan_averages,
            {'deductible': None, 'oop_max': None, 'stop_loss': None})

    def test_get_plan_averages_single_bad_response(self):
        with patch('api_wrappers.api_1.Api1Wrapper.insurance_plan_summary', new=bad_response):
            plan_averages = self.combiner.get_plan_averages('123')
            self.assertEqual(plan_averages,
               {'deductible': 1100, 'oop_max': 6000, 'stop_loss': 11500})

    def test_get_plan_averages_no_deductable(self):
        with patch('api_wrappers.api_1.Api1Wrapper.insurance_plan_summary', new=no_deductable):
            plan_averages = self.combiner.get_plan_averages('123')
            self.assertEqual(plan_averages,
               {'deductible': 1100, 'oop_max': 5666, 'stop_loss': 11000})

    def test_get_plan_averages_no_stop_loss(self):
        with patch('api_wrappers.api_1.Api1Wrapper.insurance_plan_summary', new=no_stop_loss):
            plan_averages = self.combiner.get_plan_averages('123')
            self.assertEqual(plan_averages,
               {'deductible': 1066, 'oop_max': 5666, 'stop_loss': 11500})

    def test_get_plan_averages_no_oop_max(self):
        with patch('api_wrappers.api_1.Api1Wrapper.insurance_plan_summary', new=no_oop):
            plan_averages = self.combiner.get_plan_averages('123')
            self.assertEqual(plan_averages,
               {'deductible': 1066, 'oop_max': 6000, 'stop_loss': 11000})

###############################################################################################

    def test_get_plan_mins_pass(self):
        plan_averages = self.combiner.get_plan_min('123')
        self.assertEqual(plan_averages,
            {'deductible': 1000, 'oop_max': 5000, 'stop_loss': 10000})

    @patch('api_wrappers.api_1.Api1Wrapper.insurance_plan_summary', new=bad_response)
    @patch('api_wrappers.api_2.Api2Wrapper.insurance_plan_summary', new=bad_response)
    @patch('api_wrappers.api_3.Api3Wrapper.insurance_plan_summary', new=bad_response)
    def test_get_plan_mins_all_bad_responses(self):
        plan_averages = self.combiner.get_plan_averages('123')
        self.assertEqual(plan_averages,
            {'deductible': None, 'oop_max': None, 'stop_loss': None})

    def test_get_plan_mins_single_bad_response(self):
        with patch('api_wrappers.api_1.Api1Wrapper.insurance_plan_summary', new=bad_response):
            plan_averages = self.combiner.get_plan_min('123')
            self.assertEqual(plan_averages,
               {'deductible': 1000, 'oop_max': 6000, 'stop_loss': 10000})

    def test_get_plan_mins_no_deductable(self):
        with patch('api_wrappers.api_1.Api1Wrapper.insurance_plan_summary', new=no_deductable):
            plan_averages = self.combiner.get_plan_min('123')
            self.assertEqual(plan_averages,
               {'deductible': 1000, 'oop_max': 5000, 'stop_loss': 10000})

    def test_get_plan_mins_no_stop_loss(self):
        with patch('api_wrappers.api_1.Api1Wrapper.insurance_plan_summary', new=no_stop_loss):
            plan_averages = self.combiner.get_plan_min('123')
            self.assertEqual(plan_averages,
               {'deductible': 1000, 'oop_max': 5000, 'stop_loss': 10000})

    def test_get_plan_mins_no_oop_max(self):
        with patch('api_wrappers.api_1.Api1Wrapper.insurance_plan_summary', new=no_oop):
            plan_averages = self.combiner.get_plan_min('123')
            self.assertEqual(plan_averages,
               {'deductible': 1000, 'oop_max': 6000, 'stop_loss': 10000})

###############################################################################################

    def test_get_plan_max_pass(self):
        plan_averages = self.combiner.get_plan_max('123')
        self.assertEqual(plan_averages,
            {'deductible': 1200, 'oop_max': 6000, 'stop_loss': 13000})

    @patch('api_wrappers.api_1.Api1Wrapper.insurance_plan_summary', new=bad_response)
    @patch('api_wrappers.api_2.Api2Wrapper.insurance_plan_summary', new=bad_response)
    @patch('api_wrappers.api_3.Api3Wrapper.insurance_plan_summary', new=bad_response)
    def test_get_plan_max_all_bad_responses(self):
        plan_averages = self.combiner.get_plan_averages('123')
        self.assertEqual(plan_averages,
            {'deductible': None, 'oop_max': None, 'stop_loss': None})

    def test_get_plan_max_single_bad_response(self):
        with patch('api_wrappers.api_1.Api1Wrapper.insurance_plan_summary', new=bad_response):
            plan_averages = self.combiner.get_plan_max('123')
            self.assertEqual(plan_averages,
               {'deductible': 1200, 'oop_max': 6000, 'stop_loss': 13000})

    def test_get_plan_max_no_deductable(self):
        with patch('api_wrappers.api_1.Api1Wrapper.insurance_plan_summary', new=no_deductable):
            plan_averages = self.combiner.get_plan_max('123')
            self.assertEqual(plan_averages,
               {'deductible': 1200, 'oop_max': 6000, 'stop_loss': 13000})

    def test_get_plan_max_no_stop_loss(self):
        with patch('api_wrappers.api_1.Api1Wrapper.insurance_plan_summary', new=no_stop_loss):
            plan_averages = self.combiner.get_plan_max('123')
            self.assertEqual(plan_averages,
               {'deductible': 1200, 'oop_max': 6000, 'stop_loss': 13000})

    def test_get_plan_max_no_oop_max(self):
        with patch('api_wrappers.api_1.Api1Wrapper.insurance_plan_summary', new=no_oop):
            plan_averages = self.combiner.get_plan_max('123')
            self.assertEqual(plan_averages,
               {'deductible': 1200, 'oop_max': 6000, 'stop_loss': 13000})


if __name__ == '__main__':
    unittest.main()
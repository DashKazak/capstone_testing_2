import unittest 
from unittest import TestCase
from unittest.mock import patch 

import bitcoin_price

class TestBitcoinRate(TestCase):
#     Write a test for your Bitcoin program (from the API topic) that converts a number of Bitcoin to their value in US Dollars.

# Mock the API call by providing a mock JSON response. Assert that your program calculates the correct value in dollars.

    @patch('bitcoin_price.request_rates')
    def test_currency_to_target(self, mock_rates):
        mock_rate = 1.5  # Any number will do.  
        # As long as the JSON contains the data the program needs, it does not need to be a complete response
        example_api_response = {"bpi":{"USD":{"code": "USD", "rate_float": mock_rate}}}
        mock_rates.side_effect = [ example_api_response] 
        converted = bitcoin_price.convert_bitcoin_to_target(1, 'USD')
        self.assertEqual(1.5, converted)



if __name__ == '__main__':
    unittest.main()

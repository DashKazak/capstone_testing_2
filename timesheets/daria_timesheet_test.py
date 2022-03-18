import unittest
from unittest import TestCase
from unittest.mock import patch, call

import timesheets
#python -m unittest test_timesheets.py
class TestCaseSheet(TestCase):

    @patch('builtins.input', side_effect=['2']) #patch decorator creates an input with the ,ock and it will be configured to the value when it's called
    def test_get_hours_for_day(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(2,hours)

    @patch('builtins.input', side_effect=['cat', '', '123bird', 'feufy2', '2']) #patch decorator creates an input with the ,ock and it will be configured to the value when it's called
    #side effect is a list of returned values. The first time the side effect is called in the mock it will return the first 
    #element of the list, the second time it is called it will return the second element of the list, etc. 
    #in the end we need a valid value to get rid of the infinite loops
    def test_get_hours_for_day_non_numeric_rejected(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(2,hours)

    @patch('builtins.input', side_effect=['-1', '-1000', '2'])
    def test_get_hours_for_day_hours_within_range(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(2,hours)
    
    @patch('builtins.input', side_effect=['-1', '-1000', '2'])
    def test_get_hours_for_day_hours_greater_than_0(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(2,hours)

    @patch('builtins.input', side_effect=['24.000001', '1000', '25','9'])
    def test_get_hours_for_day_hours_less_than_24(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(9,hours)
    
    @patch('builtins.print')
    def test_dispaly_total(self,mock_print):
        timesheets.display_total(123)
        mock_print.assert_called_once_with('Total hours worked: 123')
    
    @patch('timesheets.alert')
    def test_alert_meet_min_hours_doesnt_meet(self, mock_alert):
        timesheets.alert_not_meet_min_hours(12,30)
        mock_alert.assert_called_once()

    
    @patch('timesheets.alert')
    def test_alert_meet_min_hours_does_meet(self, mock_alert):
        timesheets.alert_not_meet_min_hours(40,30)
        mock_alert.assert_not_called()

    @patch('timesheets.get_hours_for_day')
    def test_get_hours(self, mock_get_hours):
        mock_hours = [5,7,9]
        mock_get_hours.side_effect = mock_hours
        days = ['m', 't', 'w']
        expected_hours = dict(zip(days, mock_hours))
        #creates a dictionary of keys and values 
        hours = timesheets.get_hours(days)
        self.assertEqual(expected_hours, hours)


    @patch('builtins.print')
    def test_display_hours(self, mock_print):
        #arrange
        example = {'M':3, 'T':12, 'W':8}
        expected_table_calls = [
            call('Day              Hours Worked              '), 
            call('M                3                         '), 
            call('T                12                        '), 
            call('W                8                         '), 
        ]
        #action
        timesheets.display_hours(example)
        mock_print.assert_has_calls(expected_table_calls)



    def test_total_hours(self):
        example = {'M':3,'T':12,'W':8.5 }
        total= timesheets.total_hours(example)
        expected_total = 3+12+8.5
        self.assertEqual(total, expected_total)


if __name__=='__main__':
    unittest.main()
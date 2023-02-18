##
# Student Name: William Zhao
# Course: CIS 502 Applied Python Programming
# Lab # 4 - Test Driver
# Application: Your Course Grade Calculator
# Description: The program tests average, variance
#              bump up, and standard deviation
# Version: Python 3.8
# Solution File: WilliamZhaoLab4Test.py.py
# Date: 02/18/23
##

#Source Code

import WilliamZhaoLab4 as as4
import unittest

class TestCases(unittest.TestCase):

    def test_case1(self):

        score_list1 = [20, 20, 20, 20, 20, 20]
        assert as4.calculate_average(*score_list1) == 20
        assert as4.bump_up(20, 20) == None
        assert as4.descriptive_stats(score_list1) == (0, 0)
        print(f'''
            #Test Case 1:

            The average lab score is: 20. Got {as4.calculate_average(*score_list1)}
            The bump up is: None. Got {as4.bump_up(20, 20)}
            The sample variance and standard deviation is: (0, 0). Got \n
            {as4.descriptive_stats(score_list1)}
        
        '''
        )

    def test_case2(self):
        score_list2 = [5, 20, 20]
        assert as4.calculate_average(*score_list2) == 15
        assert as4.bump_up(15, 5) == 10
        assert as4.descriptive_stats(score_list2) == (75, 8.66)

        print(f'''
            #Test Case 2:

            The average lab score is: 15. Got {as4.calculate_average(*score_list2)}
            The bump up is: 10. Got {as4.bump_up(15, 5)}
            The sample variance and standard deviation is: (75, 8.66). Got \n
            {as4.descriptive_stats(score_list2)}
        
        '''
        )

if __name__ == '__main__':
    unittest.main()

# Test Run Validation
"""
            #Test Case 1:

            The average lab score is: 20. Got 20.0
            The bump up is: None. Got None
            The sample variance and standard deviation is: (0, 0). Got 

            (0, 0.0)
.
            #Test Case 2:

            The average lab score is: 15. Got 15.0
            The bump up is: 10. Got 10
            The sample variance and standard deviation is: (75, 8.66). Got 

            (75, 8.66)
.
----------------------------------------------------------------------     
Ran 2 tests in 0.001s

OK
"""
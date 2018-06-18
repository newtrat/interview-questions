# The Luhn test is used by some credit card companies to distinguish valid credit card numbers from what could be a random selection of digits.
#
# Those companies using credit card numbers that can be validated by the Luhn test have numbers that pass the following test:
#
# 1. Reverse the order of the digits in the number.
# 2. Take the first, third, ... and every other odd digit in the reversed digits and sum them to form the partial sum s1
# 3. Taking the second, fourth ... and every other even digit in the reversed digits:
# 4. Multiply each digit by two and sum the digits if the answer is greater than nine to form partial sums for the even digits
# 5. Sum the partial sums of the even digits to form s2
# 6. If s1 + s2 ends in zero then the original number is in the form of a valid credit card number as verified by the Luhn test.
#
# For example, if the trial number is 49927398716:
#
# 1. Reverse the digits:
#   61789372994
# 2. Sum the odd digits:
#   6 + 7 + 9 + 7 + 9 + 4 = 42 = s1
# 3. The even digits:
#     1,  8,  3,  2,  9
#   4. Two times each even digit:
#     2, 16,  6,  4, 18
#   5. Sum the digits of each multiplication:
#     2,  7,  6,  4,  9
#   6. Sum the last:
#     2 + 7 + 6 + 4 + 9 = 28 = s2
#
# s1 + s2 = 70 which ends in zero which means that 49927398716 passes the Luhn test
#
# Task
# Write a function/method/procedure/subroutine that will validate a number with the Luhn test, and
# use it to validate the following numbers:
#
#    49927398716
#    49927398717
#    1234567812345678
#    1234567812345670

import unittest

class Luhn:
    @staticmethod
    def valid(cc):
        # YOUR CODE HERE
        return True


class TestLuhn(unittest.TestCase):

    def test(self):
        # (FEEL FREE TO ADD/CHANGE TEST CASES, TOO)
        self.assertTrue(Luhn.valid(49927398716))
        self.assertFalse(Luhn.valid(49927398717))
        self.assertTrue(Luhn.valid(1234567812345670))
        self.assertFalse(Luhn.valid(1234567812345678))

if __name__ == '__main__':
    unittest.main()

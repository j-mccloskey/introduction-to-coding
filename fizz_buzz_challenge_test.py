import unittest

from fizz_buzz_challenge import fizz_buzz


class FizzBuzzChallengeTest(unittest.TestCase):
    def test_should_print_fizz_for_multiples_of_three(self):
        self.assertEqual(fizz_buzz(3), "Fizz")
        self.assertEqual(fizz_buzz(6), "Fizz")
        self.assertEqual(fizz_buzz(9), "Fizz")

    def test_should_print_buzz_for_multiples_of_five(self):
        self.assertEqual(fizz_buzz(5), "Buzz")
        self.assertEqual(fizz_buzz(10), "Buzz")
        self.assertEqual(fizz_buzz(20), "Buzz")

    def test_should_print_fizz_buzz_when_multiples_of_both_three_and_five(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
        self.assertEqual(fizz_buzz(30), "FizzBuzz")
        self.assertEqual(fizz_buzz(300), "FizzBuzz")

    def test_should_print_the_number_itself_when_not_multiple(self):
        self.assertEqual(fizz_buzz(1), 1)
        self.assertEqual(fizz_buzz(4), 4)

import unittest
from math_quiz import generate_random_operator, calculate_result, generate_random_integer


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if the generated operator is one of '+', '-', or '*'
        for _ in range(1000):
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, ['+', '-', '*'])

    def test_function_C(self):
        test_cases = [
            (5, 2, '+', ('5 + 2', 7)),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_result in test_cases:
            problem, answer = calculate_result(num1, num2, operator)
            self.assertEqual((problem, answer), expected_result)


if __name__ == "__main__":
    unittest.main()

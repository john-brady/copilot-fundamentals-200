import unittest

class TestAmortizationCalculation(unittest.TestCase):
    def test_calculate_amortization(self):
        # Test case 1: Normal scenario
        principal = 100000
        annual_interest_rate = 5
        years = 30
        result = calculate_amortization(principal, annual_interest_rate, years)
        self.assertAlmostEqual(result, 536.82, places=2)

        # Test case 2: Zero interest rate
        principal = 100000
        annual_interest_rate = 0
        years = 30
        result = calculate_amortization(principal, annual_interest_rate, years)
        self.assertAlmostEqual(result, 277.78, places=2)

        # Test case 3: Zero years
        principal = 100000
        annual_interest_rate = 5
        years = 0
        with self.assertRaises(ValueError):
            calculate_amortization(principal, annual_interest_rate, years)

        # Test case 4: Zero principal
        principal = 0
        annual_interest_rate = 5
        years = 30
        result = calculate_amortization(principal, annual_interest_rate, years)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
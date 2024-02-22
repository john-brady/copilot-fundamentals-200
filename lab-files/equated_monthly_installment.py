def calculate_amortization(principal, annual_interest_rate, years):
    """
    Calculates the equated monthly installment (EMI) for a loan.

    Args:
        principal (float): The principal amount of the loan.
        annual_interest_rate (float): The annual interest rate as a percentage.
        years (int): The number of years for the loan.

    Returns:
        float: The calculated EMI rounded to 2 decimal places.

    Raises:
        ValueError: If years is zero.

    """
    if years == 0:
        raise ValueError("Years cannot be zero")
    if principal == 0:
        return 0
    monthly_interest_rate = annual_interest_rate / 1200
    number_of_payments = years * 12
    if annual_interest_rate != 0:
        amortization = principal * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -number_of_payments))
    else:
        amortization = principal / number_of_payments
    return round(amortization, 2)
'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

investment_amount = float(input("How much do you plan to invest?"))
Interest_Rate = float(input("What is the current price of interest rates for your currency?"))
number_of_years = float(input("How long is your investment horizon?"))
expected_value = investment_amount * (1 + Interest_Rate)**number_of_years
print(expected_value)

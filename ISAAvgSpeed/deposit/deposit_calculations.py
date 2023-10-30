import calculations.calculations

input_initial_value = float(input("Provide initial investment value: "))
input_deposit_rate = float(input("Procide deposit rate: "))
input_deposit_years = int(input("Provide number of years: "))

deposit_output_value = calculations.calculations.deposit_calculations(input_initial_value, input_deposit_rate, input_deposit_years)

print("Investment value: ", deposit_output_value)

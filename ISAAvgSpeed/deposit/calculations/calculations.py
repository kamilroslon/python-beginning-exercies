def deposit_calculations(initial_value, deposit_rate, years_of_deposit):

    deposit_value = initial_value * (1 + deposit_rate / 100) ** years_of_deposit

    return deposit_value


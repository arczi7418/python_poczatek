def calculate_deposit(entry_value, percentage,years):
    value = entry_value * (1 + percentage / 100) ** 2
    return value
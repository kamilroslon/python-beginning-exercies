def default_policy(summary_price):
    return summary_price

def loyal_customer_policy(summary_price):
    return 0.95 * summary_price

def christmas_policy(summary_price):
    if summary_price > 100:
        return summary_price - 20
    return summary_price
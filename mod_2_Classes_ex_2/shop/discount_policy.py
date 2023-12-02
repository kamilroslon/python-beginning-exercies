class DiscountPolicy:
    def apply_discount(self, summary_price):
        return summary_price

class PercentageDiscount(DiscountPolicy):
    def __init__(self, discoount_percentage):
        self.discount_percentage = discoount_percentage

    def apply_discount(self, summary_price):
        return summary_price * (100 - self.discount_percentage) / 100

class AbsoluteDiscount(DiscountPolicy):

    def __init__(self, discount_value):
        self.discount_value = discount_value

    def apply_discount(self, summary_price):
        if summary_price < self.discount_value:
            return 0
        else:
            return summary_price - self.discount_value

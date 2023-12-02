from shop.Order import Order
from shop.data_generator import order_generator
# from shop.discount_policy import loyal_customer_policy, christmas_policy
from shop.Product import Products_Expiration
from shop.Order import ExpressOrder
from shop.discount_policy import PercentageDiscount, AbsoluteDiscount

def run_example():

    random_list = order_generator()
    percentage_discount_15 = PercentageDiscount(discoount_percentage=15)
    value_discount = AbsoluteDiscount(discount_value=40)
    new_express_order_default = ExpressOrder("Kamil", "Rrrrrr", "01-12-2023", random_list)
    new_express_order_discount_percentage = ExpressOrder("Kamil", "Rrrrrr", "01-12-2023", random_list, percentage_discount_15)
    new_express_order_discount_absolute = ExpressOrder("Kamil", "Rrrrrr", "01-12-2023", random_list, value_discount)

    print(new_express_order_default)
    print(new_express_order_discount_percentage)
    print(new_express_order_discount_absolute)


if __name__ == '__main__':
    run_example()


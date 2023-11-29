from shop.Order import Order
from shop.data_generator import order_generator
from shop.discount_policy import loyal_customer_policy, christmas_policy
from shop.Product import Products_Expiration
from shop.Order import ExpressOrder

def run_example():

    random_list = order_generator()
    new_express_order = ExpressOrder("Kamil", "Rrrrrr", "01-12-2023", random_list)
    print(new_express_order)


if __name__ == '__main__':
    run_example()


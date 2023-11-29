from shop.Order import Order
from shop.data_generator import order_generator
from shop.discount_policy import loyal_customer_policy, christmas_policy
from shop.Product import Product, Expiration_Date

def run_example():


    # random_list = order_generator()
    # new_order_default = Order("Kamil", "Rrrr", random_list, None)
    # new_order_loyalty = Order("Kamil", "Rrrr", random_list, discount_policy=loyal_customer_policy)
    # new_order_christmas = Order("Kamil", "Rrrr", random_list, discount_policy=christmas_policy)
    #
    # print(new_order_default)
    #
    # print(new_order_default.summary_price)

    new_product = Expiration_Date("Some apple", "Some category", 4, 4, 2022, 2)
    new_product.does_expire()


if __name__ == '__main__':
    run_example()


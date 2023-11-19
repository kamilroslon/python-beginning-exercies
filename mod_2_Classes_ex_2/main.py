from shop.Order import Order
from shop.discount_policy import loyal_customer_policy, christmas_policy


# def return_to_sort(order):
#     return order.summary_price
def run_example():
    # fife_orders = []
    # for list_element in range(5):
    #     random_list = Order.generate_random_list()
    #     new_order = Order("Kamil", "RRrrr", random_list)
    #     fife_orders.append(new_order)
    #
    # fife_orders.sort(key= lambda Order: Order.summary_price)
    # # fife_orders.sort(key=return_to_sort())
    # for list_element in fife_orders:
    #     print(list_element)

# def run_example2():
#     random_list = Order.generate_random_list()
#     new_order = Order("Kamil", "Rrrr", random_list)
#     print(new_order)

    random_list = Order.generate_random_list()
    new_order_default = Order("Kamil", "Rrrr", random_list, None)
    new_order_loyalty = Order("Kamil", "Rrrr", random_list, discount_policy=loyal_customer_policy)
    new_order_christmas = Order("Kamil", "Rrrr", random_list, discount_policy=christmas_policy)

    print(new_order_default)
    print(new_order_loyalty)
    print(new_order_christmas)


if __name__ == '__main__':
    run_example()


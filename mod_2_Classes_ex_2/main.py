from shop.Order import Order
from shop.data_generator import order_generator
from shop.Product import Products_Expiration
from shop.Order import ExpressOrder
from shop.discount_policy import PercentageDiscount, AbsoluteDiscount

def run_example():

    random_list = order_generator()
    percentage_discount_15 = PercentageDiscount(discoount_percentage=15)
    value_discount = AbsoluteDiscount(discount_value=40)
    new_order = Order("Kamil", "rrrrr", random_list, discount_policy=None)
    new_express_order_default = ExpressOrder("Kamil", "Rrrrrr", "01-12-2023", random_list)
    new_express_order_discount_percentage = ExpressOrder("Kamil", "Rrrrrr", "01-12-2023", random_list, percentage_discount_15)
    new_express_order_discount_absolute = ExpressOrder("Kamil", "Rrrrrr", "01-12-2023", random_list, value_discount)

    # print(new_express_order_default)
    # print(new_express_order_discount_percentage)
    # print(new_express_order_discount_absolute)
    # print(len(str(new_express_order_discount_absolute)) * "#")
    # # for item in new_express_order_default.elements_list:
    # #     print(item)
    # print(new_order)
    #
    # print(new_order.return_dict)
    # print(new_order.return_dict_plus)
    #
    # dict_one = new_order.return_dict
    # # dict_two = new_order.return_dict_plus
    # # print(dict_one.update(dict_two))
    # dict_one.update(new_order.return_dict_plus)
    # print(dict_one)
    #

    some_dict = {element.identifier: element for element in random_list}
    print(some_dict)

if __name__ == '__main__':
    run_example()


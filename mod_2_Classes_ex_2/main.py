from shop.Order import Order
from shop.data_generator import order_generator
from shop.Product import Products_Expiration
from shop.Order import ExpressOrder
from shop.discount_policy import PercentageDiscount, AbsoluteDiscount
from shop.Product import Product
from collections import namedtuple

Apple = namedtuple("Apple", ["name", "size", "price_per_kg"])
def test_tuple_products():

    parameters = [("Name", 1, 1, 2, 2, "Name", 1, 1, 2, 2, True), ("Name1", 1, 1, 2, 2, "Name1", 1, 1, 2, 2, True), ("Name2", 1, 2, 2, 2, "Name2", 1, 2, 2, 3, False)]
    for params in parameters:
        name, category, unit_price, pieces, identifier, name1, category1, unit_price1, pieces1, identifier1 , expected_results = params
        results = Product(name, category, unit_price, pieces, identifier) == Product(name1, category1, unit_price1, pieces1, identifier1)
        if results == expected_results:
            print("Passed")
        else:
            print("Not Passed")

def named_tuple():

    apple = Apple("TestApple", 4, 4)
    print(apple.name)
    print(apple[0])

    for attribute in apple:
        print(attribute)

def run_example():

    random_list = order_generator()
    percentage_discount_15 = PercentageDiscount(discoount_percentage=15)
    value_discount = AbsoluteDiscount(discount_value=40)
    new_order = Order("Kamil", "rrrrr", random_list, discount_policy=None)
    new_express_order_default = ExpressOrder("Kamil", "Rrrrrr", "01-12-2023", random_list)
    new_express_order_discount_percentage = ExpressOrder("Kamil", "Rrrrrr", "01-12-2023", random_list, percentage_discount_15)
    new_express_order_discount_absolute = ExpressOrder("Kamil", "Rrrrrr", "01-12-2023", random_list, value_discount)

    some_dict = {element.identifier: element for element in random_list}
    print(some_dict)

    new_expired_product = Products_Expiration("Test", 2, 2.4, 5, 6, 2021, 1)

    print(new_expired_product.does_expire())




if __name__ == '__main__':
    run_example()
    # named_tuple()
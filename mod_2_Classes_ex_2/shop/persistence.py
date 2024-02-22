import os
from shop.Order import Order
def save_order(order):
    orders_data_path = os.path.join("data", "orders.txt")
    with open(orders_data_path, mode="a") as orders_file:
        orders_file.write(str(order))
        orders_file.write("\n")

def load_order():
    orders_data_path = os.path.join("data", "orders.txt")
    with open(orders_data_path, mode="r") as orders_file:
        return orders_file.read()


def init_order():
    firstname = input("WHat is your name? ")
    lastname = input("What is your last name? ")
    return Order(firstname, lastname)
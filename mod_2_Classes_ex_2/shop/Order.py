class Order:
    def __init__(self, first_name, last_name, products_list=None):
        self.first_name = first_name
        self.last_name = last_name
        if products_list is None:
            products_list = []
        self.products_list = products_list
        self.summary_price = calculate_order(products_list)

def calculate_order(products_list):
    total_price = 0
    for product in products_list:
        total_price += product.unit_price
    return total_price

def print_order_summary(order):
    print("First name: ", order.first_name)
    print("Last name: ", order.last_name)
    print("Summary: ", order.summary_price)
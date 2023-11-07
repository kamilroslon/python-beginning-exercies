class Order:
    def __init__(self, first_name, last_name, elements_list=None):
        self.first_name = first_name
        self.last_name = last_name
        if elements_list is None:
            elements_list = []
        self.elements_list = elements_list
        # total_price = 0
        # for product in products_list:
        #     total_price += product.unit_price * product.pieces
        self.summary_price = self.calculate_prices()

    def __str__(self):
        elements = ""
        for element in self.elements_list:
            elements += "\n"
            elements += f"Product: {element.name} | Pieces: {element.pieces} | Price per piece: {element.unit_price} | Total row: {element.unit_price * element.pieces}"
        elements += "\n" * 2
        elements += f"First name: {self.first_name} | Last name: {self.last_name} | Order value: {self.summary_price}"
        return elements

    def __len__(self):
        return len(self.elements_list)

    def calculate_prices(self):
        total_price = 0
        for element in self.elements_list:
            total_per_row = element.unit_price * element.pieces
            total_price += total_per_row
        return total_price


class OrderElement:
    def __init__(self, Order):
        self.find_elements(Order)

    def find_elements(self, Order):
        for product in Order.products_list:
            sum_order_entry = product.unit_price * product.pieces
            print(f"Product's name: {product.name} | Unit price: {product.unit_price} | Pieces: {product.pieces} | Row's total: {sum_order_entry}")
from shop.Product import Product
from shop.discount_policy import DiscountPolicy
import random
class Order:

    MAX_ELEMENTS = 20
    def __init__(self, first_name, last_name, elements_list=None, discount_policy=None):
        self.first_name = first_name
        self.last_name = last_name
        if elements_list is None:
            elements_list = []
        if len(elements_list) > Order.MAX_ELEMENTS:
            elements_list = elements_list[:Order.MAX_ELEMENTS]
        self._elements_list = elements_list
        # total_price = 0
        # for product in products_list:
        #     total_price += product.unit_price * product.pieces
        self.summary_tax = self._calculate_tax()
        if discount_policy is None:
            discount_policy = DiscountPolicy()
        self.discount_policy = discount_policy

    def __str__(self):
        elements = ""
        for element in self._elements_list:
            elements += "\n"
            elements += f"Product: {element.name} | Pieces: {element.pieces} | Price per piece: {element.unit_price} | Total row: {element.unit_price * element.pieces} | Category: {element.category_name} | Tax rate: {TaxCalculator.show_tax_rate(element)} | Tax value: {TaxCalculator.calculate_tax(element)}"
        elements += "\n" * 2
        elements += f"First name: {self.first_name} | Last name: {self.last_name} | Order value: {self.summary_price} | Tax value: {self.summary_tax:.2f}"
        return elements

    def __len__(self):
        return len(self._elements_list)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if len(self._elements_list) != len(other._elements_list):
            return False
        if self.first_name != other.first_name or self.last_name != other.last_name:
            return False
        for element in self._elements_list:
            if element not in other._elements_list:
                return False
        return True

    @property
    def elements_list(self):
        return self._elements_list

    @property
    def summary_price(self):
        return self._calculate_prices()

    @elements_list.setter
    def elements_list(self, value):
        if len(value) < Order.MAX_ELEMENTS:
            self._elements_list = value
        else:
            self._elements_list = value[:Order.MAX_ELEMENTS]

    def _calculate_prices(self):
        total_price = 0
        for element in self._elements_list:
            total_per_row = element.unit_price * element.pieces
            total_price += total_per_row
        return self.discount_policy.apply_discount(total_price)

    def _calculate_tax(self):
        total_tax = 0
        for element in self._elements_list:
            total_tax_row = TaxCalculator.calculate_tax(element)
            total_tax += total_tax_row
        return total_tax

    def add_product_to_order(self, name, category, unit_price, pieces):
        if len(self._elements_list) < self.MAX_ELEMENTS:
            new_product = Product(name, category, unit_price, pieces)
            self._elements_list.append(new_product)
            self.summary_price = self._calculate_prices()
        else:
            print ("\n")
            print(f"Too much elements in list, product will not be added")

class OrderElement:
    def __init__(self, Order):
        self.find_elements(Order)

    def find_elements(self, Order):
        for product in Order.products_list:
            sum_order_entry = product.unit_price * product.pieces
            print(f"Product's name: {product.name} | Unit price: {product.unit_price} | Pieces: {product.pieces} | Row's total: {sum_order_entry}")


class TaxCalculator:

    TAX_VALUE_5 = 5
    TAX_VALUE_8 = 8
    TAX_VALUE_20 = 20

    @staticmethod
    def calculate_tax(element):
        if element.category_name % 3 == 0:
            tax_value = element.unit_price * element.pieces * TaxCalculator.TAX_VALUE_5/100
        elif element.category_name % 2 == 0:
            tax_value = element.unit_price * element.pieces * TaxCalculator.TAX_VALUE_8 / 100
        else:
            tax_value = element.unit_price * element.pieces * TaxCalculator.TAX_VALUE_20 / 100
        return tax_value

    @staticmethod
    def show_tax_rate(element):
        if element.category_name % 2 == 0:
            tax_rate = TaxCalculator.TAX_VALUE_8/100
        elif element.category_name % 3 == 0:
            tax_rate = TaxCalculator.TAX_VALUE_5 / 100
        else:
            tax_rate = TaxCalculator.TAX_VALUE_20 / 100
        return tax_rate

class ExpressOrder(Order):

    DELIVERY_FEE = 13
    def __init__(self, first_name, last_name, order_date, elements_list=None, discount_policy=None):
        super().__init__(first_name, last_name, elements_list, discount_policy)
        self.order_date = order_date
        self.summary_with_delivery = self.price_with_delivery()
    def price_with_delivery(self):
        return super()._calculate_prices() + ExpressOrder.DELIVERY_FEE
    def __str__(self):
        return f"First name: {self.first_name}, Last name: {self.last_name}, Delivery date: {self.order_date}, Delivery fee: {self.DELIVERY_FEE}, Subtotal: {self.summary_price}, Total with delivery: {self.summary_with_delivery}"
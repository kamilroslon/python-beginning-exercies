from shop.Product import Product
from shop.discount_policy import DiscountPolicy
from shop.Error import ElementsInOrderLimit
import random


class Order:
    MAX_ELEMENTS = 20

    def __init__(
        self, first_name, last_name, elements_list=None, discount_policy=None
    ):
        self.first_name = first_name
        self.last_name = last_name
        if elements_list is None:
            elements_list = []
        self.elements_list = elements_list
        self.summary_tax = self._calculate_tax()
        if discount_policy is None:
            discount_policy = DiscountPolicy()
        self.discount_policy = discount_policy

    def __str__(self):
        elements = ""
        for element in self._elements_list:
            elements += "\n"
            elements += f"Identifier: {element.identifier} | Product: {element.name} | Pieces: {element.pieces} | Price per piece: {element.unit_price} | Total row: {element.unit_price * element.pieces} | Category: {element.category_name} | Tax rate: {TaxCalculator.show_tax_rate(element)} | Tax value: {TaxCalculator.calculate_tax(element)}"
        elements += "\n" * 2
        elements += f"First name: {self.first_name} | Last name: {self.last_name} | Order value: {self.summary_price} | Tax value: {self.summary_tax:.2f}"
        return elements

    # def __len__(self):
    #     return len(self._elements_list)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if len(self._elements_list) != len(other._elements_list):
            return False
        if (
            self.first_name != other.first_name
            or self.last_name != other.last_name
        ):
            return False
        for element in self._elements_list:
            if element not in other._elements_list:
                return False
        return True

    @property
    def elements_list(self):
        return self._elements_list

    @elements_list.setter
    def elements_list(self, value):
        if len(value) > Order.MAX_ELEMENTS:
            allowed_limit = Order.MAX_ELEMENTS
            raise ElementsInOrderLimit(
                allowed_limit=allowed_limit,
                message=f"Too many elements, limit is: {allowed_limit}",
            )
        self._elements_list = value

    @property
    def summary_price(self):
        return self._calculate_prices()

    @property
    def return_dict(self):
        order_elements_dict = {
            element.identifier: element for element in self._elements_list
        }
        return order_elements_dict

    @property
    def return_dict_plus(self):
        order_elements_dict_plus = {
            element.identifier + 1: element for element in self._elements_list
        }
        return order_elements_dict_plus

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
        if len(self._elements_list) >= Order.MAX_ELEMENTS:
            raise ElementsInOrderLimit(allowed_limit=Order.MAX_ELEMENTS)
        new_product = Product(name, category, unit_price, pieces)
        self._elements_list.append(new_product)
        self.summary_price()

class OrderElement:
    def __init__(self, Order):
        self.find_elements(Order)

    def find_elements(self, Order):
        for product in Order.products_list:
            sum_order_entry = product.unit_price * product.pieces
            print(
                f"Product's name: {product.name} | Unit price: {product.unit_price} | Pieces: {product.pieces} | Row's total: {sum_order_entry}"
            )


class TaxCalculator:
    FIVE_CATEGORY = [5, ["BAKERY", "FRUIT_AND_VEGETABLES", "FRESH_MEAT"]]
    EIGTH_CATEGORY = [8, ["VEGAN_BIO"]]
    TWENTY_CATEGORY = [20, [""]]

    @staticmethod
    def calculate_tax(element):
        if element.category_name in TaxCalculator.FIVE_CATEGORY[1]:
            tax_value = (
                element.unit_price
                * element.pieces
                * TaxCalculator.FIVE_CATEGORY[0]
                / 100
            )
        elif element.category_name in TaxCalculator.EIGTH_CATEGORY:
            tax_value = (
                element.unit_price
                * element.pieces
                * TaxCalculator.EIGTH_CATEGORY[0]
                / 100
            )
        else:
            tax_value = (
                element.unit_price
                * element.pieces
                * TaxCalculator.TWENTY_CATEGORY[0]
                / 100
            )
        return tax_value

    @staticmethod
    def show_tax_rate(element):
        if element.category_name in TaxCalculator.EIGTH_CATEGORY[1]:
            tax_rate = TaxCalculator.EIGTH_CATEGORY[0] / 100
        elif element.category_name in TaxCalculator.FIVE_CATEGORY[1]:
            tax_rate = TaxCalculator.FIVE_CATEGORY[0] / 100
        else:
            tax_rate = TaxCalculator.TWENTY_CATEGORY[0] / 100
        return tax_rate


class ExpressOrder(Order):
    DELIVERY_FEE = 13

    def __init__(
        self,
        first_name,
        last_name,
        order_date,
        elements_list=None,
        discount_policy=None,
    ):
        super().__init__(first_name, last_name, elements_list, discount_policy)
        self.order_date = order_date

    @property
    def price_with_delivery(self):
        return super()._calculate_prices() + ExpressOrder.DELIVERY_FEE

    def __str__(self):
        return f"First name: {self.first_name}, Last name: {self.last_name}, Delivery date: {self.order_date}, Delivery fee: {self.DELIVERY_FEE}, Subtotal: {self.summary_price}, Total with delivery: {self.price_with_delivery}"

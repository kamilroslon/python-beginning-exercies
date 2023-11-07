class Product:
    pass

class Order:
    pass

if __name__ == '__main__':

    apple_1 = Product()
    apple_2 = Product()
    potato_1 = Product()
    potato_2 = Product()

    print(type(apple_1))
    print(type(potato_2))

    dict_products = {"apple1": apple_1,
                     "apple2": apple_2,
                     "potato1": potato_1,
                     "potato2": potato_2}

    order = ["oeder_1", "order_2", "order_3", dict_products]

    print(order)

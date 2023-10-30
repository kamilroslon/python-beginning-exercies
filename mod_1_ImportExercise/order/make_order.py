from .products import products_list, update_product_quantity

orders = [
    {
        "product": "bread",
        "quantity": 4,
        "total_price": 16
    }
]


def create_new_order(product_name, quanity):
    price = products_list[product_name]["price"]
    available_quantity = products_list[product_name]["quantity"]

    if available_quantity < quanity:
        print("Stock is not sufficient")
        return None

    total_price = price * quanity
    new_order = {
        "product": product_name,
        "quantity": quanity,
        "total_price": total_price
    }
    update_product_quantity(product_name, quanity)
    orders.append(new_order)
    return new_order

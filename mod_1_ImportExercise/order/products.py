products_list = {
    "bread":{
        "quantity": 50,
        "price": 4
    },
    "apple":{
        "quantity": 20,
        "price": 1
    },
    "eggs": {
        "quantity": 30,
        "price": 3
    },
    "butter":{
        "quantity": 7,
        "price": 6
    }
}

def update_product_quantity(product_name, ordered_quantity):
    products_list[product_name]["quantity"] -= ordered_quantity
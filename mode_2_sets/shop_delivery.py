import random

def products_delivery():

    available_products = ["apple", "banana", "butter", "milk", "tortilla pie", "potatos", "cheese", "cookies"]
    return [available_products[random.randint(0,7)] for _ in range(5)]
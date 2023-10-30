from order.make_order import create_new_order

def run_shop():
    print("Welcome!!!")
    product_name = input("Provide product name: ")
    product_quantity = int(input("Provide product quantity: "))

    result = create_new_order(product_name, product_quantity)
    if result is not None:
        total_price = result["total_price"]
        print(f"Total order value {total_price}")

if __name__ == "__main__":
    run_shop()